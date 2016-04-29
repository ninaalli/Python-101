Object Oriented Programming PartII

Inheritance allows us to organize our code every more regarding objects
The local method takes precedent over the parent method

Pseudo Code
  Comment out the code to ensure future you and others can understand what the code is meant to do
  
PUDB
  You must debug systematically.
  Here's an online tutorial: http://heather.cs.ucdavis.edu/~matloff/pudb.html

Inside your terminal make use of
  help()
  dir()
  doc_strings = """ This Is A Doc String """
  Open a file inside Python REPL using -i
  python3 -i my_file.py
  
Class.__init__ vs. def __init__ vs. super
  For a single class, no need to use super
  Parent/Child class can use it. 
    Its automatically inherited, its only for usage when you want to override something
    
Complicated Methods of OOP
  Class methods vs. Static methods
Python Methods and How They Work - https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods
