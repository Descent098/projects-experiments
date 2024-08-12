[Julia](https://julialang.org/) is a language developed in 2012 primarily for data science. It is mostly intended to be an amalgamation of existing data analysis languages (python, R, MATLAB etc.), with the intention of making it easy to do common data science tasks faster.

To run the examples install Julia based on the instructions [here](https://julialang.org/downloads/). Then add the code examples to a file ending in `.jl`, you can then run them using `julia <filename>.jl`, or you can run the examples interactively by running `julia` then typing in the examples.

Here is an example of a function that takes in a string and returns a string:

```julia
function greet(name::string) string
  return "Hello $(name)!"
end

greet("Kieran")
```

Here is another example of iterating over a list (Array):

```julia
function printShoppingList(shoppingList::Array{string})
  println("Your shopping list:")
  for (index,item) in enumerate(shoppingList)
      println("$(index). $(item)")
  end
end

printShoppingList(["Milk", "Eggs", "Bread"])
```

Typing is optional, so this is also valid:

```julia
function printShoppingList(shoppingList)
  println("Your shopping list:")
  for (index,item) in enumerate(shoppingList)
      println("$(index). $(item)")
  end
end

printShoppingList(["Milk", "Eggs", "Bread"])
```