Variable: 

List: most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]).

Dictionary: The dictionary allows you to associate one piece of data (a "key") with another (a "value"). The analogy comes from real-life dictionaries, where we associate a word (the "key") with its meaning. You can create a dictionary with {}; What makes dictionaries so useful is that we can give meaning to the items within them.

*By combining lists and dictionaries you can describe basically any data structure used in computing.

Data Type: Python has five standard data types
      Numbers
      String
      List
      Tuple - A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.
      Dictionary

Data Structure:
      x = 3          # numbers
      a = "gorillas" # strings
      t = True       # booleans



Iterate:

Invoke:

Instantiate:


Parameters vs arguments:

Object Oriented Programming:
Class: A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.
Class variable: A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.
Data member: A class variable or instance variable that holds data associated with a class and its objects.
Function overloading: The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.
Instance variable: A variable that is defined inside a method and belongs only to the current instance of a class.
Inheritance: The transfer of the characteristics of a class to other classes that are derived from it.
Instance: An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.
Instantiation: The creation of an instance of a class.
Method : A special kind of function that is defined in a class definition.
Object: A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods.
Operator overloading: The assignment of more than one function to a particular operator.
Inheritance: allows multiple base classes, a derived class can override any methods of its base class or classes, and a method can call the method of a base class with the same name.

Python supports four different numerical types −
    int (signed integers)
    long (long integers, they can also be represented in octal and hexadecimal)
    float (floating point real values)
    complex (complex numbers)
    
Control Flow:
Loops: allows us to execute a statement or group of statements multiple times. 
  while loop: Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.
  for loop: Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.
  nested loops: You can use one or more loop inside any another while, for or do..while loop.
  
Control Statements: 
  break statement: Terminates the loop statement and transfers execution to the statement immediately following the loop.
  continue statement: Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
  pass statement: The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

White Space: 
      Determines where a loop repeats itself by the indentation in the whitespace
      
Branches: 
      basically only one kind of branch in Python, the 'if' statement. The simplest form of the if statement simple executes a block of code only if a given predicate is true, and skips over it if the predicate is false. 
      can also add "elif" (short for "else if") branches onto the if statement. If the predicate on the first “if” is false, it will test the predicate on the first elif, and run that branch if it’s true. If the first elif is false, it tries the second one, and so on. Note, however, that it will stop checking branches as soon as it finds a true predicate, and skip the rest of the if statement. You can also end your if statements with an "else" branch. If none of the other branches are executed, then python will run this branch.
