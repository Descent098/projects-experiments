import traceback
from platform import platform
from dataclasses import dataclass
from ctypes import c_void_p, cdll, Structure, c_char_p, c_int, POINTER, byref

# import library
if platform().lower().startswith("windows"):
    lib = cdll.LoadLibrary("./lib.dll")
else:
    lib = cdll.LoadLibrary("./lib.so") 


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

