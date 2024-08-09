Simula was a language created in the 1960's based on ALGOL. It is considered the first object oriented language. It created the idea of classes and objects.

Huge thank you to Deus In Machina who's [post](https://www.deusinmachina.net/p/simula-the-forgotten-programming) made it possible to get simula running for me (all normal GNU variants were broken on WSL, linux and windows). Install the latest Java Open JDK then head to [the download link](https://portablesimula.github.io/github.io/#:~:text=and%20run%20Simula.-,Simula%20Download,-NOTE%3A%20If%20setup). From there open the `.jar` file it downloaded, and open your `.sim` file with the code. 

For example here is some code for an `Animal` class with two string attributes `Nam` (Name is reserved), and `Species` as well as a constructor (called `initialize` that you have to write yourself) and another method called `greet`:

```simula
BEGIN
  class Animal;
    BEGIN
      text Nam, Species; ! Instance Variables;
      procedure initialize(currentName, spec);
        text currentName, spec;
          BEGIN
            Nam:- currentName;
            Species:- spec;
          END; ! END of initialize();
      procedure greet;
        begin
          OutText("Hello ");
          OutText(Nam);
          OutText(" the ");
          OutText(Species);
        END; ! END of greet();
    end; ! END of Animal;


  ! Testing Animal Class;
  ref(Animal) Tiger; 

  Tiger:- new Animal;
  Tiger.initialize("Jody", "Tiger")
  Tiger.greet;

END
```

This code would print "Hello Jody the Tiger".