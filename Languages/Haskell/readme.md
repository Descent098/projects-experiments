Haskell is a purely functional language developed in 1990 developed by the  International Conference on Functional Programming committee to develop an open functional language. It is (besides all the various forms of [Lisp](https://en.wikipedia.org/wiki/Lisp_(programming_language))) the most popular purely functional language.

You can test Haskell code without installing it in the [Haskell Playground](https://play.haskell.org/). To install Haskell you should use [GHCup](https://www.haskell.org/ghcup/) which is a manager for your Haskell installation. It will install everything for you, and help you manage your Haskell versions. Follow the steps on the site to get everything you need setup. You can then copy the examples into `.hs` files and then run using `runghc <filename>.hs`, or you can compile and run using `ghc <filename>.hs` to compile, then `./<filename>` to run the binary.

Here is an example program that defines a function called `greet()` that takes in a string called name and returns that string with "Hello " placed before it:

```haskell
greet :: String -> String
greet name = "Hello " ++ name

-- Runs the program
main :: IO ()
main = do
    putStrLn (greet "Kieran")
```

Here is a program that prints a shopping list with it's index next to it:

```haskell
-- Takes in a list of strings in and print them with their index
printShoppingList :: [String] -> IO ()
printShoppingList items =
    mapM_ putStrLn [show idx ++ ". " ++ item | (idx, item) <- zip [1..] items]


-- Runs the program
main :: IO ()
main = do
    putStrLn "Shopping List"
    putStrLn "============="
    printShoppingList ["Eggs", "Ham", "Spam"]
```