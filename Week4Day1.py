Ternary Operators
>>>turtle = True
>>>print ("I like turtles") if turtle else print ("boo")
#need an else statement in there to make it work
#there is no speed benefit to this, but it will give you the opp for a one liner
    #do something is something is true
    
Multiple else's can be put in here, but readability counts

List Comprehensions 
allows us to build a list of values by filtering through an interable. 
They give you speed, it goes through the powers of magnitude. 

List comprehensions provide a short and concise way to create lists. It consists of square brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists. The result would be a new list made after the evaluation of the expression in context of the if and for clauses.

>>>vowels = 'aeiouAEIOU'
>>>my_string = 'Jeff is very cool and tall and smart.'
>>>my_string_vowels = [x for x in my_my string if x in vowels]
>>>my_string_vowels
['e', i, e, o, o, a, a, a, a,]
>>>my_vowels = []

EXERCISE: any for loop can be made into a list comprehension
  go from for loop to this list comprehension, once you have the four loop working
  
Generators - Controllers - Class Methods
Generators are iterators, but you can only iterate over them once. It’s because they do not store all the values in memory, they generate the values on the fly. You use them by iterating over them, either with a ‘for’ loop or by passing them to any function or construct that iterates. Most of the time generators are implemented as functions. However, they do not return a value, they yield it. Here is a simple example of a generator function:

def generator_function():
    for i in range(10) *2:
        yield i

for item in generator_function():
    print(item)

# Output: 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

Generators are best for calculating large sets of results (particularly calculations involving loops themselves) where you don’t want to allocate the memory for all results at the same time. Many Standard Library functions that return lists in Python 2 have been modified to return generators in Python 3 because generators require fewer resources.



http://book.pythontips.com/en/latest/ternary_operators.html
