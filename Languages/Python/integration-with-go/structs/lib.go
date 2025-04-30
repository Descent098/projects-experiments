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
import (
	"unsafe"

	"github.com/brianvoe/gofakeit/v7"
)

type User struct {
	name  string
	age   int
	email string
}

func createRandomUser() *User {
	return &User{gofakeit.Name(), 21, gofakeit.Email()}
}

func CreateRandomUsers(count int) *[]User {
	result := make([]User, count)
	for i := range count {
		result[i] = *createRandomUser()
	}
	return &result
}

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

//export free_user
func free_user(userReference *C.User) {
	C.free(unsafe.Pointer(userReference.name))
	C.free(unsafe.Pointer(userReference.email))
	C.free(unsafe.Pointer(userReference))
}

func main() {
	// Do nothing
}
