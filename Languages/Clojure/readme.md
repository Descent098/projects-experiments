Lisp is a programming language developed in the 1960's. It supports multiple paradigms, but was the first to allow for higher order functions, recursion, and a ton of other computer science concepts[^4] including those that allow for functional programming. It is the language that inspired many other functional languages such as [scheme](https://www.scheme.org/) (which itself inspired [Idris](https://www.idris-lang.org/)), and most importantly [clojure](https://clojure.org/) etc. 


These files are made for [clojure](https://clojure.org/), a specific dialect of lisp. You can install it following the instructions on [this page](https://clojure.org/), Clojure is designed to run in a [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop), but you also put contents into a `.clj` file. 

A tip for reading this code to make it easier is that statements in lisp are in [polish notation](https://en.wikipedia.org/wiki/Polish_notation). So for example `(- n 1)` is using the function `-` (subtract) over the arguments `n` and `1`. So `(- n 1)` would be the same as `n-1` in other languages. Also execution of function requires parenthesis around the function calls, so:

```clojure
user=> format "Hello %s" "World!"
```

Would not call the function, but instead would return information about it:

```clojure
user=> format "Hello %s" "Hello"
#object[clojure.core$format 0x6979efad "clojure.core$format@6979efad"]
"Hello %s"
"Hello"
```

To call the function, encapsulate it in parenthesis:

```clojure
user=> (format "Hello %s" "Hello")
"Hello Hello"
````

