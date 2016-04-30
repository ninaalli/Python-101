Python with CompSci

A Linked List stores data in nodes
Each node will contain two things. A value that node is storing, and a pointer that will point to the next node in the list
The first node in a linked list is known as the head.

With linked list we are not storing/declaring our data set initially. Instead we are only looking at one node at a time. This will save us memory.
The advantage to this versus an array/list is we will not use as much memory to navigate through a list of values.
Imagine if we had an extremely large data set. We wouldn't want to store it in memory just to loop through it.
The disadvantage to this is since we are not declaring all the values up front we do not have the ability to start a search at a specific point in time. We have to loop through every node until we find what we want.

Big O Notation is a way to check/describe how efficient an algorithm is. That is how long it takes to run
Looping through a list of items in a linear fashion will be a O(n)
Having a loop nested inside of another loop will be an O(n^2)
Using the Binary Search would be a O(logn)

Stacks are abstract data types. Like Linked List this is a concept that is programmable in multiple languages
This follows the LIFO process. (Last In First Out)
Every node holds a value and a pointer to the next node

The main methods to quickly display stacks are pop and append (push in other lanuages)
pop will remove the top node on the stack and return it to you
append will add a node to the top of the stack

Queues are also abstract data types, but they work in the opposite way of stacks. That is they follow the FIFO process (First In, First Out)
Imagine an array/list normally (not turned 90 degrees like the stack diagram)
Enqueue - add a node to the end of the queue
Dequeue - to remove a node from the front of the queue



