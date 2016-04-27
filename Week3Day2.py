String and List are iterable.

Week#/Day1For DB-why would you need more than one instance?

SQL JOINS
*#1 thing that slows down a website is the db querying*

Foreign Keys go to the MANY instance
id INCREMENT PRIMARY KEY AUTOINCREMENT will auto add the key for you.

print("Destroying old data") - it will delete the info that is already in there

type cat in command line to bring in items from Bash/Terminal

Join is to hit two tables at once and get one result
INNER JOIN - commonly used,you have to tell it the foreign key

Look at the various SQL joins: http://www.codeproject.com/Articles/33052/Visual-Representation-of-SQL-Joins


Example Code:
controller
​
class User:
​
    def login:
        checks to see if the un and pw is in db
        returns t if theyre there
        false is theyre now
​
    def get permission
        another call to db to get permission
        returns 1 if client
        returns 2 if bankers
        returns None if neither
​
​
    def welcomescreen_banker
        shows banker menu
        just call a view function
        potentiially get back a choice
​
    def welcomescreen_client
        shows banker menu
        just call a view function
        potentiially get back a choice
​
controller
​
class Run:
​
    def run
        while login != true
            give some error message
            login
​
        permission = get_permission
​
        if permission == 1
            welcomescreen_clienbt
​
        elif permission == 2
            welcomescreen_client
​
