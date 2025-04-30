from ctypes import cdll, c_char_p
from platform import platform

# import library
if platform().lower().startswith("windows"):
    lib = cdll.LoadLibrary("./lib.dll")
else:
    lib = cdll.LoadLibrary("./lib.so") 

# Simple idempotent function call
result = lib.Greeting()

# Variadic function (with arguments/returns)
lib.GreetS.argtypes = [c_char_p]
lib.GreetS.restype = c_char_p

name = "Kieran".encode() # Convert string to bytes
greeting = lib.GreetS(name)

print(greeting.decode("utf-8"))
