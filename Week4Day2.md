ORM = PYthon + SQL - take SQL queries and use them over and over again, by using their method name.
ORM - object relational mapper, not strictly for wrapping in Python. Also see MOngo
ORM is a concept for multiple frameworks

Build your own ORM

SELECT * FROM Artist; <-- Python  Artist.all() <-- ORM

Multiple conditions SELECT * FROM  Artist WHERE name = "Linkin Park";
  ORM Artist.filter(name = "Linkin Park"
  
Re-usable codes are a plus!

Shouldnt matter what the tables are, should be able to use .method, .function the same way

**kwargs is a HUGE help!
.all is going to be dynamic, for current and future self or others to use

if the class variable is configured to appear as (day, month, year) put @classmethod above what you are trying to define and it will appear

class with cls.__NAME__
  SELECT * FROM cls.__NAME__
  
  have to plan it out
  
  Arg, Kwarg, Class __ name, 
  
  
.all, .filter, 
Tomorrow is a big day for planning it.
setattr() - can be used for this. 
