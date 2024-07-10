# Iterators
An iterator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. The Python iterators object is initialized using the iter() method. It uses the next() method for iteration.

- **__iter__():**
    - The **iter()** method is called for the initialization of an iterator. This returns an iterator object.

- **__iter__():**
    - The next method returns the next value for the iterable. When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object, which further uses the next() method to iterate over. This method raises a StopIteration to signal the end of the iteration.

**Example:**
```Python
string = "GFG"
ch_iterator = iter(string)
 
print(next(ch_iterator))
print(next(ch_iterator))
print(next(ch_iterator))
```

**Output:**
```
G
F
G
```

## Creating and looping over an iterator using iter() and next()
Below is a simple Python **Iterator** that creates an iterator type that iterates from 10 to a given limit. For example, if the limit is 15, then it prints 10 11 12 13 14 15. And if the limit is 5, then it prints nothing.

**Example:**
```Python
# An iterable user defined type
class Test:
 
    # Constructor
    def __init__(self, limit):
        self.limit = limit
 
    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self
 
    # To move to next element. In Python 3,
    # we should replace next with __next__
    def __next__(self):
 
        # Store current value ofx
        x = self.x
 
        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration
 
        # Else increment and return old value
        self.x = x + 1;
        return x
 
# Prints numbers from 10 to 15
for i in Test(15):
    print(i)
 
# Prints nothing
for i in Test(5):
    print(i)
```

**Output:**
```
10
11
12
13
14
15
```

## Iterating over built-in iterable using iter() method
In the following iterations, the iteration state and iterator variable is managed internally (we can’t see it) using an iterator object to traverse over the built-in iterable like *list*, *tuple*, *dict*, etc.

**Example:**
```Python
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
     
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
     
# Iterating over a String
print("\nString Iteration")    
s = "Geeks"
for i in s :
    print(i)
     
# Iterating over dictionary
print("\nDictionary Iteration")   
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for key, value in d.items() :
    print(f"{key}   {value}")
```

**Output:**
```
List Iteration
geeks
for
geeks

Tuple Iteration
geeks
for
geeks

String Iteration
G
e
e
k
s

Dictionary Iteration
xyz  123
abc  345
```

## Iterable vs Iterator
Python iterable and Python iterator are different. The main difference between them is, iterable in Python cannot save the state of the iteration, whereas in iterators the state of the current iteration gets saved.

**Note:**
Every iterator is also an iterable, but not every iterable is an iterator in Python. 

### Iterating on an Iterable
```Python
tup = ('a', 'b', 'c', 'd', 'e')
 
for item in tup:
    print(item)

```

**Output:**
```
a
b
c
d
e
```

### Iterating on an iterator
```Python
tup = ('a', 'b', 'c', 'd', 'e')
 
# creating an iterator from the tuple
tup_iter = iter(tup)
 
print("Inside loop:")
# iterating on each item of the iterator object
for index, item in enumerate(tup_iter):
    print(item)
 
    # break outside loop after iterating on 3 elements
    if index == 2:
        break
 
# we can print the remaining items to be iterated using next()
# thus, the state was saved
print("Outside loop:")
print(next(tup_iter))
print(next(tup_iter))
```

**Output:**
```
Inside loop:
a
b
c
Outside loop:
d
e
```

## Getting StopIteration Error while using iterator
Iterable in Python can be iterated over multiple times, but iterators raise **StopIteration Error** when all items are already iterated.
Here, we are trying to get the next element from the iterator after the completion of the for-loop. Since the iterator is already exhausted, it raises a **StopIteration Exception**. Whereas, using an iterable, we can iterate on multiple times using for loop or can get items using indexing.

```Python
iterable = (1, 2, 3, 4)
iterator_obj = iter(iterable)
 
print("Iterable loop 1:")
# iterating on iterable
for item in iterable:
    print(item, end=",")
 
print("\nIterable Loop 2:")
for item in iterable:
    print(item, end=",")
 
print("\nIterating on an iterator:")
# iterating on an iterator object multiple times
for item in iterator_obj:
    print(item, end=",")
 
print("\nIterator: Outside loop")
# this line will raise StopIteration Exception
# since all items are iterated in the previous for-loop
print(next(iterator_obj))
```

**Output:**
```
Iterable loop 1:
1,2,3,4,
Iterable Loop 2:
1,2,3,4,
Iterating on an iterator:
1,2,3,4,
Iterator: Outside loop

Traceback (most recent call last):
  File "scratch_1.py", line 21, in <module>
    print(next(iterator_obj))
StopIteration
```