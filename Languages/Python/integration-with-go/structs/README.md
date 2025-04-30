# Structs

Structs are known for being more complex to deal with, this is because both in Go and Python you are essentially disabling the GC, which means you need to allocate and deallocate your memory. Additionally you need to setup a mapping in C so it understands what's happening.

## Setting up Go

To get started on the Go size you will need to setup a typedef for a C struct in the comments above the import, for example:

```go
package main

/*
#include <stdlib.h>

typedef struct{
	char* name;
	int age;
	char* email;
} User;
*/
import "C"

// The go version of the struct in C
type User struct {
	name  string
	age   int
	email string
}
```

I used the same names because when we want to use the C version of the struct we use `*C.User`, and the go version is just the plain `User` or `*User`. Now let's look at creating a function to instantiate a struct using random values:

```go
//export create_random_user
func create_random_user() *C.User {
	// Create a random go version of the user
	res := createRandomUser()

	// Create go versions of variables
	goName := res.name
	goEmail := res.email
	age := res.age

	// Create C-compatible versions of variables
	cName := C.CString(goName)
	cEmail := C.CString(goEmail)

	// Allocate necessary memory
	user := (*C.User)(C.malloc(C.size_t(unsafe.Sizeof(C.User{}))))

	// Assign values to freshly created struct
	user.name = cName
	user.age = C.int(age)
	user.email = cEmail

	return user
}
```

Here is an example function that takes in values to allocate a struct:

```go
//export create_user
func create_user(name *C.char, age int, email *C.char) *C.User {
	// Allocate necessary memory for new struct
	user := (*C.User)(C.malloc(C.size_t(unsafe.Sizeof(C.User{}))))

	// Assign values to new struct
	user.name = name
	user.age = C.int(age)
	user.email = email

	return user
}
```

Looks great right? Wrong, this will actually break. Even though the string is in the right form, python will potentially GC the string when you pass it in, so you have to copy the data first so a copy of it exists in go:

```go
//export create_user
func create_user(name *C.char, age C.int, email *C.char) *C.User {
	// Allocate necessary memory for new struct
	user := (*C.User)(C.malloc(C.size_t(unsafe.Sizeof(C.User{}))))

	// Copy strings into Go-managed memory
	cName := C.CString(C.GoString(name))
	cEmail := C.CString(C.GoString(email))

	// Assign values
	user.name = cName
	user.age = age
	user.email = cEmail

	return user
}
```

Now we also need a function to free the necessary memory that we instantiated:

```go
//export free_user
func free_user(userReference *C.User) {
	C.free(unsafe.Pointer(userReference.name))
	C.free(unsafe.Pointer(userReference.email))
	C.free(unsafe.Pointer(userReference))
}
```

This third function is pretty scary because we really need to be careful that we're not doing a [double free](https://owasp.org/www-community/vulnerabilities/Doubly_freeing_memory) by accident. 

## Setting up Python

The python setup is relatively simple. To start, let's import the DLL, setup the structs and the functions:

```python
from ctypes import c_void_p, cdll, Structure, c_char_p, c_int, POINTER

# Load the DLL
lib = cdll.LoadLibrary("./lib.dll")

# Define the C-compatible User struct in Python
class User(Structure):
    _fields_ = [
        ("name", c_char_p),
        ("age", c_int),
        ("email", c_char_p),
    ]

# Set function return/arg types
lib.create_random_user.restype = POINTER(User)
lib.free_user.argtypes = [POINTER(User)]

# Call the function
user_ptr = lib.create_random_user()
user = user_ptr.contents

print(f"Name: {user.name.decode()}")
print(f"Age: {user.age}")
print(f"Email: {user.email.decode()}")

# Clean up memory
lib.free_user(user_ptr)
```

We can then call the function to create the user, and inspect it's values via the `Pointer.contents`:

```python
# Call the function
user_ptr = lib.create_random_user()
user = user_ptr.contents
```

Remember that strings in C are not encoded, they're just bytes, so to get them back as strings, we need to decode them:
```python
print(f"Name: {user.name.decode()}")
print(f"Age: {user.age}")
print(f"Email: {user.email.decode()}")
```

Then remember to cleanup afterwards:

```python
# Clean up memory
lib.free_user(user_ptr)
```


So the full example is:

```python
from ctypes import c_void_p, cdll, Structure, c_char_p, c_int, POINTER

# Load the DLL
lib = cdll.LoadLibrary("./lib.dll")

# Define the C-compatible User struct in Python
class User(Structure):
    _fields_ = [
        ("name", c_char_p),
        ("age", c_int),
        ("email", c_char_p),
    ]

# Set function return/arg types
lib.create_random_user.restype = POINTER(User)
lib.free_user.argtypes = [POINTER(User)]

# Call the function
user_ptr = lib.create_random_user()
user = user_ptr.contents

print(f"Name: {user.name.decode()}")
print(f"Age: {user.age}")
print(f"Email: {user.email.decode()}")

# Clean up memory
lib.free_user(user_ptr)
```


### Improvements with a Wrapper

Because of all the back and forth data constraints and the allocation-cleanup process, I would recommend wrapping this sort of struct in a class, for example:

```python
from dataclasses import dataclass
from ctypes import c_void_p

... # omitted library setup code

@dataclass
class User:
    name:str
    age:int
    email:str
    _pointer: c_void_p
    
    @classmethod
    def create(cls:'User')->'User':
        pointer = lib.create_random_user()
        data = pointer.contents
        return User(data.name.decode(), data.age, data.email.decode(), pointer)

    def __del__(self):  
        # Free's the memory used by the struct on deletion
        print(f"Cleaning {self.name} pointer at: {self._pointer}")
        lib.free_user(self._pointer)
```

I personally like the addage of using a `C` prefix for classes that are the C structs, and then just the normal name for the python versions. So a full example is:

```python
import traceback
from dataclasses import dataclass
from ctypes import c_void_p, cdll, Structure, c_char_p, c_int, POINTER, byref

# Load the DLL
lib = cdll.LoadLibrary("./lib.dll")

# Define the C-compatible User struct in Python
class CUser(Structure):
    _fields_ = [
        ("name", c_char_p),
        ("age", c_int),
        ("email", c_char_p),
    ]

# Set function return/arg types
lib.create_random_user.restype = POINTER(CUser)
lib.free_user.argtypes = [POINTER(CUser)]

lib.create_user.restype = POINTER(CUser)
lib.create_user.argtypes = [c_char_p, c_int, c_char_p]

@dataclass
class User:
    name:str
    age:int
    email:str
    _pointer: c_void_p
    
    @classmethod
    def create_user(cls:'User', name:str, age:int, email:str) -> 'User':
        pointer = lib.create_user(name.encode(encoding="utf-8"), age, email.encode(encoding="utf-8"))
        data = pointer.contents
        try:
            assert data.name.decode() == name
            assert data.age == age
            assert data.email.decode() == email
        except (AssertionError, UnicodeDecodeError) as e:
            # Something went wrong, free the memory
            lib.free_user(pointer)
            raise ValueError(f"Could not instantiate User\n\t{repr(traceback.format_exception(e))}")
        return User(data.name.decode(), data.age, data.email.decode(), pointer)
    
    @classmethod
    def create_random_user(cls:'User')->'User':
        pointer = lib.create_random_user()
        data = pointer.contents
        return User(data.name.decode(), data.age, data.email.decode(), pointer)

    def __del__(self):  
        # Free's the memory used by the struct on deletion
        print(f"Cleaning {self.name} pointer at: {self._pointer}")
        lib.free_user(self._pointer)
```

We can now use the wrapper easily with:

```python
from wrapper import User

# Create a single user
k = User.create_user("Kieran", 26, "kieran@canadiancoding.ca")
print(f"Here is me: {k}")

# Create a bunch of random Users

r:list[User] = []
for i in range(10):
    r.append(User.create_random_user())

from pprint import pprint
pprint(r) # pretty-print the list
```

Which will give us:

```bash
~/projects-experiments/Languages/Python/integration-with-go/structs>python testing.py
Here is me: User(name='Kieran', age=26, email='kieran@canadiancoding.ca', _pointer=<user_library.LP_CUser object at 0x000001771CA372D0>)
[User(name='Jordane Champlin',
      age=21,
      email='malliearmstrong@jones.org',
      _pointer=<user_library.LP_CUser object at 0x000001771CA37550>),
 User(name='Pierre Boyle',
      age=21,
      email='cloydborer@dubuque.info',
      _pointer=<user_library.LP_CUser object at 0x000001771CA374D0>),
 User(name='Alfreda Jacobson',
      age=21,
      email='aronrunolfsdottir@terry.name',
      _pointer=<user_library.LP_CUser object at 0x000001771CA375D0>),
 User(name='Santiago Kling',
      age=21,
      email='hertacruickshank@walsh.io',
      _pointer=<user_library.LP_CUser object at 0x000001771CA37650>),
 User(name='Jennings Keeling',
      age=21,
      email='adelleschmitt@wehner.org',
      _pointer=<user_library.LP_CUser object at 0x000001771CA376D0>),
 User(name='Garry Kessler',
      age=21,
      email='selinarutherford@orn.info',
      _pointer=<user_library.LP_CUser object at 0x000001771CA37750>),
 User(name='Lucius Bergnaum',
      age=21,
      email='randallwilderman@conroy.io',
      _pointer=<user_library.LP_CUser object at 0x000001771CA377D0>),
 User(name='Jevon Johnston',
      age=21,
      email='ivakerluke@tremblay.info',
      _pointer=<user_library.LP_CUser object at 0x000001771CA37850>),
 User(name='Xavier Wilkinson',
      age=21,
      email='ebbabrown@emard.com',
      _pointer=<user_library.LP_CUser object at 0x000001771CA378D0>),
 User(name='Nova Ruecker',
      age=21,
      email='miastark@heller.net',
      _pointer=<user_library.LP_CUser object at 0x000001771CA379D0>)]
Cleaning Kieran pointer at: <user_library.LP_CUser object at 0x000001771CA372D0>
Cleaning Nova Ruecker pointer at: <user_library.LP_CUser object at 0x000001771CA379D0>
Cleaning Xavier Wilkinson pointer at: <user_library.LP_CUser object at 0x000001771CA378D0>
Cleaning Jevon Johnston pointer at: <user_library.LP_CUser object at 0x000001771CA37850>
Cleaning Lucius Bergnaum pointer at: <user_library.LP_CUser object at 0x000001771CA377D0>
Cleaning Garry Kessler pointer at: <user_library.LP_CUser object at 0x000001771CA37750>
Cleaning Jennings Keeling pointer at: <user_library.LP_CUser object at 0x000001771CA376D0>
Cleaning Santiago Kling pointer at: <user_library.LP_CUser object at 0x000001771CA37650>
Cleaning Alfreda Jacobson pointer at: <user_library.LP_CUser object at 0x000001771CA375D0>
Cleaning Pierre Boyle pointer at: <user_library.LP_CUser object at 0x000001771CA374D0>
Cleaning Jordane Champlin pointer at: <user_library.LP_CUser object at 0x000001771CA37550>
```
