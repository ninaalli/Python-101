??? methods for how to use the math operations

you cannot iterate over numbers. 

use elif and else under if, otherwise IF will continue to rotate continually.

when there is a new function added in, it will look back up the stack

Python is single threaded and operates on a stack
Recursion can get confusing very quickly . . .

recursion - take your iteration loop. each recursive call is a new call
  the function calls itself again to do the operation to repeat
  
fibonacci - https://technobeans.wordpress.com/2012/04/16/5-ways-of-fibonacci-in-python/

BaseCase - recursion is always moving toward it. It cleans up the logic; 

once a return runs, none of the code beneath it will hit.

Control + Command + arrow up/down will move a whole line up/down

****it didnt satisfy these two conditions - head and heart. . . so appropriate for today***

classes
  list, dictionaries
  -datetime
    month/day/year/hour/minutes/seconds
      year - month - day hour:month:sec
      strf: return it in the format you requested
      naïve date will not change
        time delta will return the proper hour (decreases by seconds)
        parsing dates is a huge pain in the ass
        relies on caps and lower case 
        
        TO BRING IN DATETIME
        >>> import datetime
>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_divide_and_round', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
>>> import datetime as d   <<<this will require less writing
  bound method requires () after the name
  >>> d.datetime.now()
datetime.datetime(2016, 5, 11, 11, 34, 57, 927999)


>>> now = d.datetime.now()
>>> now
datetime.datetime(2016, 5, 11, 11, 35, 30, 817076)
>>> dir(now)
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
>>> 
strp - parse (have to look at this and make sense of it)
strf - does not have the year, month, day
  
  >>> now.strftime("%c")   WHAT is c mean?
strptime(...) method of builtins.type instance
    string, format -> new datetime parsed from a string (like time.strptime()).


HIT Q TO GET out OF HELP 

'Wed May 11 11:35:30 2016'

  -sets
    collection of unique items, only holds immutable items
    order is not nec guaranteed
  
  -tuples
    if you add something to a tuple, it will create a new tuple with 
      the tuple is unchanging.
      lists are always changing
      they are mutable
      can get the union of the two sets
      Enumerate - first value is the index key, the second is the locator value

things that are in order: can be unpacked
