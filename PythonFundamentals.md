Words to Know: 
Invoke - call the function
Iterate - loop over


Variable:
  take a name and assign it a value
  any object in Python
  everything in Python is an object
  cant stand with a #, cannot declare with special character, written in snake case (ie janine_medina)
  all variables will be snake_case, no caps
  the longer the name, the better bc it is a better indication of what it is
  
  Data Types
Strings
Strings are immutable. Once they are declared they cannot be changed. You can add strings together to create a new string but you cannot mutate an already existing one
Numbers
  Floats (if you convert a decimal to an integer, you will lose the decimal)
    decimals (decimal object)
  Integers
    whole number
  Booleans
    True
    False
    
0 is a False value, as in always

Math Operators and Boolean Operators
supports PEMDAS
== equal to
!= not equal to
<= less than or equal to
>= greater than or equal to
< less than
> greater than

REPL - read, evaluate, print, loop
Type in Python3 and you can work from the terminal
inas-Air:~ ninaalli$ python3
Python 3.5.1 (default, Apr  6 2016, 11:17:42) 
[GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 8+8
16
>>> "A"=="A" and 8==8
if the value it hits last as False it will return the value
and short circuits at the first false
or short circuit at the first true
for float and integer, it will convert them as one or the other


for variables: 
name on the left, string on the right.

integers, tuples, and strings are immutable.
  lists and dictionaries are mutable.
  
  Mutable - can change the value
  Immutable - cannot change
  strings are immutable
  
literal syntax - create a list (lists are mutable) need to add parenthesis
m. means methods (FIND THE LIST)
  >>> h = m = r= ["word"]
  >>> r
  ['word']
  >>> .m


***make a new string object, bc strings are immutable
  
in the repl write dir <built-in function dir>
to invoke it - >>> dir ()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'h', 'm', 'r']

>>> dir(h)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

anything without an __ is a 
  
import statement - how we bring in something to the Python file.
module is a toolkit we can bring in (Easter Egg - import this)

Obj Types
-Strings
-Integers
-Floats
-Lists
-Dictionaries

>>> help()

Welcome to Python 3.5's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.5/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> dict

Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if D has a key k, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 
 We subscript with the name as a string ie -janine()
 
 **key value pair = name/value pairs
 **we cannot on the fly, add new index numbers
  with dictionary, we can assign key/value pairs
  keep consistency within the list to maintain working with the same data type (great for data mining)
  
  if you hit the variable nina. (hit tab) will show you all the values or you can hit dir(nina)
  
  dir("")
    shows all the methods to deal with strings
    >>> dir("")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

    
  dir(str)
  >>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

for a class to say its a class, it has to impliment it

vars(nina)

look at the different options as you are working on it-esp the methods within the interface

if does not need a condition
else/elif need a condition

Lists and Indexing
  avoid lists with various data types
  
Function - a block of code that can be reused.
  def my_name():
    print ("My name is Nina")
Functions are not associated with a class.

DRY - Dont Repeat Yourself
  encapsulate that in a function, if something changes you change it in one place
  
Function creates a scope:
  variables that it has access to
  
when the function is created, it has domain over the items inside it (local scope)

Dont use global variables, creates entanglement, creates a reliance where they may not have dominance over.

function declaration:
if we put items in the () we say how to define it.

dir prints everything in the local space
the ones outside 

>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> def scope_test():
...   print ("inside function")
...   print (dir())
... 
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'scope_test']
>>> scope_test()
inside function
[]

**we want our functions to be functional and not global: 
   it looks at: 
      Local, Enclosing, Global, Builtin
      if you had a function within a function, it will look at local, there wont be an enclosing, then go to global
      
we cant manipulate a string outside, we cant reassign it

Syntactical Sugar***
performing an assignment - cant use an assignment if it hasnt been defined in the local space
when you say something equals something r=r, it is in the local scope

DONT USE GLOBAL, pass it in as a parameter

!!For loop
for <loop variable> in <collection>

!!while loop runs until a condition is false, you control the condition.

assignment has to happen before use, it doesnt exist before use. 

Start, Stop, Step 
(start is where it will begin)
(stop is what place it will stop at)
(step is how it will increment)
Range is defined in the Builtin (DONT NAME IT THAT WAY)
if you mess it up (del insert name here)

recursive functions: fx that calls upon itself.

Iteration with list, iteration with strings, 
fibonacci, do all the 1's first

