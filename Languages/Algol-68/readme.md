ALGOL is a language created in the 1950's designed to do various types of computation. It is the inspiration for tons of languages that came after it, like C.

You can run the example using [ALGOL Genie](https://jmvdveer.home.xs4all.nl/en.download.algol-68-genie-current.html) (I used ALGOL 68 version 3), install or download an executable then add content to a `.a68` file and run using `a68g.exe <filename>.a68`. This is a program in ALGOL 68 that prints `"Hello <name>"` where the name is the name variable:

```algol
BEGIN
  COMMENT Define variables COMMENT

  STRING name;

  name := "Kieran";

  COMMENT Print result COMMENT

  print(("Hello, ", name, "!", newline))

END
```

You can then define procedures (functions), which can return or not. For example this code defines two procedures, greet which returns nothing, and prints the `name` provided to it, and `concat_with_spaces` which takes in a list of strings, and returns them concatenated together with spaces:

```algol
BEGIN
  # Takes in a name and prints "Hello <name>" #
  PROC greet = (STRING name) VOID:
  BEGIN
    print(( "Hello ", name, newline ))
  END;

  # Takes in a list of strings and concatenates the strings with spaces #
  PROC concat_with_spaces = (REF [] STRING strings) STRING:
  BEGIN
    STRING result := "";
    FOR i FROM LWB strings TO UPB strings DO
        result := result + strings[i];
        IF i < UPB strings THEN
          result := result + " "
        FI
    OD;
    result # Return result #
  END;

  # Test greet() #
  STRING name := "Kieran";
  greet(name); # Prints "Hello Kieran" #

  # Test concat_with_spaces() #
  [2] STRING array := ("Hello", "world!");
  STRING concatenated := concat_with_spaces(array);
  print((concatenated, newline)); # Prints "Hello World!" #

END
```

This prints:

```
Hello Kieran
Hello World!
```