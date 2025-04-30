# Dynamically linking go with python

Python can be slow at the best of times, but switching to another language can waste a ton of your time rewritting. Instead, is it worth it to integrate libraries written in other languages for the slow parts of python, and use python for the rest? What are the pros and cons to doing this?


## Why bother?

The idea is performance, go is faster than python, but is it really worth it? I made a quick benchmark by implementing a scraper to grab details of a site, parse them and add them to an item. So, how much performance are we actually talking about:

```
pure_python_scraping took 9.528015851974487 seconds for 49 sites
Site.from_urls took 1.176224946975708 seconds for 49 sites

pure_python_scraping took 24.260991096496582 seconds for 99 sites
Site.from_urls took 2.8018906116485596 seconds for 99 sites
```

Quite a bit apparently, these tests were run for 4 workers in python, what if we crank that to 10:

```
pure_python_scraping took 15.578768014907837 seconds for 99 sites
Site.from_urls took 2.696641683578491 seconds for 99 sites
```

This decreases the time, but what about the CPU utilization and memory?

```
pure_python_scraping took 18.09375023841858 seconds for 99 sites with max CPU usage of 3.5
Site.from_urls took 4.515949249267578 seconds for 99 sites with max CPU usage of 2.0
```

However when I refined the test, and included memory:

```
pure_python_scraping took 17.39162588119507 seconds for 99 sites with:
        Max CPU usage of 1.8
        Max RAM usage of: 70.0 %
Site.from_urls took 4.625860929489136 seconds for 99 sites with:
        Max CPU usage of 1.9
        Max RAM usage of: 70.4 %
Memory difference is 0.4000000000000057% of 33444192256
        133776769.02400188B
        130641.0KB
        127.0MB 
```

Meaning that the memory overhead is slightly higher on golang, likely because of how many objects are being created and passed back and forth


## The approach


1. Create a [.dll](https://en.wikipedia.org/wiki/Dynamic-link_library) or [.so](https://stackoverflow.com/questions/9809213/what-are-a-and-so-files)
2. Call from python using `ctypes.cdll`


## Setup

Cgo requires a C compiler to work. Most people like GCC, personally I have been using [zig](https://ziglang.org/download/) which is a different language entirely, but it's fully C compatible, and is cross platform.

<details><summary>Linux/MacOS</summary>

You will need GCC installed, this should be pre-packaged on Linux/MacOS, to test open a terminal and type `gcc`

If you don't see it, you can also instead install [zig](https://ziglang.org/download/), which is what I used

</details>

<details><summary>Windows</summary>

For windows there are a few choices, I personally would recommend [`zig cc`](https://ziglang.org/download/). 

Others recommend [`miniGW`](https://sourceforge.net/projects/mingw/) and [`TDM-GCC`](https://sourceforge.net/projects/tdm-gcc/), neither worked for me on windows. Specifically if you're getting this error below:

```bash
# runtime/cgo
cc1: sorry, unimplemented: 64-bit mode not compiled in
```

Then switch to [zig](https://ziglang.org/download/)

</details>

Once you have GCC/Zig installed you should be good to go, but if you get errors try running `go env` and making sure the CC variable is set to the correct path (can run `which gcc`/`which zig` on linux/macOS and `where gcc`/`where zig` on windows to find the path). If it's not set correctly, set the path using:

```bash
go env -w CC=$PathToCompiler
```

If you installed zig, then the path will be `path/to/zig cc`, so for me I installed zig in `C:\binaries\zig-windows-x86_64-0.14.0-dev.2613+0bf44c309\zig.exe` so I ran:

```bash
go env -w CC="C:\binaries\zig-windows-x86_64-0.14.0-dev.2613+0bf44c309\zig.exe cc"
```

## Preparing the Go Code

You will need to create a DLL compatible library, to do this you will need to add `//export <funcName>` (no space) to export it to the DLL file (remember to also capitalize to make the function public). For example:

```go
package main

import "C"  // The C library must be imported

import "fmt"

//export Greeting
func Greeting() {
    fmt.Println("Hello from Go!")
}

func main() {
    // Do nothing
}
```

Keep in mind that some types are more complex than others, for example to have a string function, you need something like:

```go
//export GreetS
func GreetS(name *C.char) *C.char {
	goName := C.GoString(name) // Convert C string to a go string
	result := fmt.Sprintf("HELLO %s", goName) // Process string
    // Return a C-compatible string
	return C.CString(result) 
}
```

If you forget to do this you will get an error in python with something like:

```py
OSError: exception: access violation reading 0x0000000000000000
```


To compile go to a dll you will need to run platform dependent compile scripts:

<details><summary>Linux/Mac</summary>

`go build -buildmode=c-shared -o lib.so lib.go`

</details>

<details><summary>Windows</summary>

`go build -buildmode=c-shared -o lib.dll lib.go`

</details>


## Running in python

Running in python is pretty simple, just import the library, and use it like a module to run functions:

```python
from ctypes import cdll

from platform import platform

# import library
if platform().lower().startswith("windows"):
    lib = cdll.LoadLibrary("./lib.dll")
else:
    lib = cdll.LoadLibrary("./lib.so") 

# Call Greeting in python
lib.Greeting()
```

For more complicated functions, you need to typehint your arguments and return types to make sure python knows what to do:

```python
from ctypes import cdll, c_char_p
from platform import platform

# import library
if platform().lower().startswith("windows"):
    lib = cdll.LoadLibrary("./lib.dll")
else:
    lib = cdll.LoadLibrary("./lib.so") 

# Tell python what the function is
lib.GreetS.argtypes = [c_char_p]
lib.GreetS.restype = c_char_p

name = "Kieran".encode() # Convert string to bytes
greeting = lib.GreetS(name)

print(greeting.decode("utf-8"))
```

## References

- go
  - https://github.com/go101/go101/wiki/CGO-Environment-Setup
  - https://gist.github.com/zchee/b9c99695463d8902cd33
  - https://go.dev/wiki/cgo
  - https://github.com/brianvoe/gofakeit (data faking lib I used)
  - https://stackoverflow.com/questions/64574831/how-to-return-struct-from-cgo
  - https://leapcell.io/blog/enhancing-python-speed-using-go
- Python
  - https://docs.python.org/3/library/ctypes.html#loading-dynamic-link-libraries
  - https://stackoverflow.com/questions/8447308/ctypes-and-string
  - https://stackoverflow.com/questions/5081875/ctypes-beginner
  - https://www.turing.com/kb/ctypes-modules-and-their-implementation-in-python
