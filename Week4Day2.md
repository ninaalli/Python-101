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


Classmethod as explained on StackOverflow:
http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner
Though classmethod and staticmethod are quite similar, there's a slight difference in usage for both entities: classmethod must have a reference to a class object as the first parameter, whereas staticmethod can have no parameters at all.

Let's look at all that was said in real examples.

Boilerplate

Let's assume an example of a class, dealing with date information (this is what will be our boilerplate to cook on):

class Date(object):

   day = 0
   month = 0
   year = 0

   def __init__(self, day=0, month=0, year=0):
       self.day = day
       self.month = month
       self.year = year
This class obviously could be used to store information about certain dates (without timezone information; let's assume all dates are presented in UTC).

Here we have __init__, a typical initializer of Python class instances, which receives arguments as a typical instancemethod, having the first non-optional argument (self) that holds reference to a newly created instance.

Class Method

We have some tasks that can be nicely done using classmethods.

Let's assume that we want to create a lot of Date class instances having date information coming from outer source encoded as a string of next format ('dd-mm-yyyy'). We have to do that in different places of our source code in project.

So what we must do here is:

Parse a string to receive day, month and year as three integer variables or a 3-item tuple consisting of that variable.
Instantiate Date by passing those values to initialization call.
This will look like:

day, month, year = map(int, string_date.split('-'))
date1 = Date(day, month, year)
For this purpose, C++ has such feature as overloading, but Python lacks that feature- so here's when classmethod applies. Lets create another "constructor".

   @classmethod
   def from_string(cls, date_as_string):
       day, month, year = map(int, date_as_string.split('-'))
       date1 = cls(day, month, year)
       return date1

date2 = Date.from_string('11-09-2012')
Let's look more carefully at the above implementation, and review what advantages we have here:

We've implemented date string parsing in one place and it's reusable now.
Encapsulation works fine here (if you think that you could implement string parsing as a single function elsewhere, this solution fits OOP paradigm far better).
cls is an object that holds class itself, not an instance of the class. It's pretty cool because if we inherit our Date class, all children will have from_string defined also.
Static method

What about staticmethod? It's pretty similar to classmethod but doesn't take any obligatory parameters (like a class method or instance method does).

Let's look at the next use case.

We have a date string that we want to validate somehow. This task is also logically bound to Date class we've used so far, but still doesn't require instantiation of it.

Here is where staticmethod can be useful. Let's look at the next piece of code:

   @staticmethod
   def is_date_valid(date_as_string):
       day, month, year = map(int, date_as_string.split('-'))
       return day <= 31 and month <= 12 and year <= 3999

   # usage:
   is_date = Date.is_date_valid('11-09-2012')
So, as we can see from usage of staticmethod, we don't have any access to what the class is- it's basically just a function, called syntactically like a method, but without access to the object and it's internals (fields and another methods), while classmethod does.
