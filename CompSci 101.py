n = the run time of the operations
  this is like a mathematical equation
n = iterating over something
constant time to go over something
O(1) - for every time the individual operation will take.
  the Big O on this is O(3n)
  
  |
n |
  |
  |
  |____________________________
    Operations
    
  The only one concerning us is the most significant value
  as n gets larger, 3 has less and less of an impact
  
Best case is n2 (n sqauared)
nested for loops is n2
triple nested for loops - n3 is a bad idea

Matrix Sort  - n
memorize them? but why?

Big O algorithm
there are many worst case scenarios

Big O Runtimes
C(onstant) 1
log(n) - reduces decision by 1/2
n
nlogn - this is the combined
n2 - horrible time
n3 - super bad
2n - traveling salesman issue - how to get to all the places in a quick way

nlogn is the fastest sort
n2 is the slowest sort

Bubble sort:
you go one time all the way through the first time
the closest is n2 to what we are looking for

Linked List
information about hte rest of the files. nodes are the building blocks of the linked list
  has two things- data and a reference to the next node
    this is a sturcutre that we will create
    next.node - another node or none
    
    nodes live in arbitrary locations in the memory
    linked list have no concept of how long they are
   
   Head node            tail node
      ^                 ^
    data      data     data
    ---- ->   ---- ->   ----  -> none
    next      next      next
    
this structure exists throughout programming, crucial to understanding data structures

Python list is optimized to do things-operate under optimal conditions.
List - iterate through it
Search  | n
add     | n
remove  | n
reverse | n

Benes of a list:
index into a list, therefore has knowledge of its size. this is expensive - this has to reindex if you add, expand.
add is n
lose is n

important to do it in the right order
to reverse it reverse the pointers in the same order as they were added

Big O is time complexity
Space Complexity is amount of space

reset the list as it moves from head to the none
nl.oldhead is the head of the list, next = current.next, keep pushing the top one all the way down

