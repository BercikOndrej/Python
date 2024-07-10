# Module Collections
The collection Module in Python provides different types of containers. A Container is an object that is used to store different objects and provide a way to access the contained objects and iterate over them. Some of the built-in containers are `Tuple`, `List`, `Dictionary`, etc. In this article, we will discuss the different containers provided by the collections module.

Here is a summary of module. More details information is in [Python docs](https://docs.python.org/3/).

Provided containers:
- **Counters**
- **OrderedDict**
- **DefaultDict**
- **ChainMap**
- **NamedTuple**
- **DeQue**
- **UserDict**
- **UserList**
- **UserString**

# Counters
A **counter** is a sub-class of the dictionary. It is used to keep the count of the elements in an iterable in the form of an unordered dictionary where the key represents the element in the iterable and value represents the count of that element in the iterable.

**Note:** It is equivalent to bag or multiset of other languages.

## Initializing Counter Objects
The counter object can be initialized using the counter() function and this function can be called in one of the following ways:

- With a sequence of items
- With a dictionary containing keys and counts
- With keyword arguments mapping string names to counts

**Example:**
```Python
from collections import Counter 
  
# With sequence of items  
print(Counter(['B','B','A','B','C','A','B',
               'B','A','C']))
  
# with dictionary 
print(Counter({'A':3, 'B':5, 'C':2}))
  
# with keyword arguments 
print(Counter(A=3, B=5, C=2))
```
**Output:**
```
Counter({'B': 5, 'A': 3, 'C': 2})
Counter({'B': 5, 'A': 3, 'C': 2})
Counter({'B': 5, 'A': 3, 'C': 2})
```

# OrderedDict
An **OrderedDict** is also a sub-class of dictionary but unlike dictionary, it remembers the order in which the keys were inserted. 

**Example:**
```Python
from collections import OrderedDict 
  
print("This is a Dict:\n") 
d = {} 
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
  
for key, value in d.items(): 
    print(key, value) 
  
print("\nThis is an Ordered Dict:\n") 
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
for key, value in od.items(): 
    print(key, value) 
```

**Output:**
```
This is a Dict:

a 1
b 2
c 3
d 4

This is an Ordered Dict:

a 1
b 2
c 3
d 4
```

While deleting and re-inserting the same key will push the key to the last to maintain the order of insertion of the key.

**Example:**
```Python
from collections import OrderedDict 


od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
print('Before Deleting')
for key, value in od.items(): 
    print(key, value) 
    
# deleting element
od.pop('a')

# Re-inserting the same
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items(): 
    print(key, value)
```

**Output:**
```
Before Deleting
a 1
b 2
c 3
d 4

After re-inserting
b 2
c 3
d 4
a 1
```

# DefaultDict
**Defaultdict** is a container like **dictionaries** present in the module collections. Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.

default_factory is a function that provides the default value for the dictionary created. If this parameter is absent then the KeyError is raised.

**Initializing DefaultDict Objects**

DefaultDict objects can be initialized using `DefaultDict()` method by passing the data type as an argument.

**Example:**
```Python
from collections import defaultdict

    
# Defining the dict and passing 
# lambda as default_factory argument
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
```

**Output:**
```
1
2
Not Present
```

**__missing__():** This function is used to provide the default value for the dictionary. This function takes default_factory as an argument and if this argument is None, a KeyError is raised otherwise it provides a default value for the given key. This method is basically called by the **__getitem__()** method of the dict class when the requested key is not found. **__getitem__()** raises or return the value returned by the **__missing__()**. method.

**Example:**

```Python
from collections import defaultdict

    
# Defining the dict
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

# Provides the default value 
# for the key
print(d.__missing__('a'))
print(d.__missing__('d'))
```

**Output:**
```
Not Present
Not Present
```

# ChainMap
A **ChainMap** encapsulates many dictionaries into a single unit and returns a list of dictionaries.

**Example:**
```Python
from collections import ChainMap 
   
   
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap 
c = ChainMap(d1, d2, d3) 
   
print(c)
```

**Output:**
```
ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
```

## Accessing Keys and Values from ChainMap
Values from **ChainMap** can be accessed using the key name. They can also be accessed by using the `keys()` and `values()` method.

**Example:**
```Python
from collections import ChainMap 
   
   
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap 
c = ChainMap(d1, d2, d3) 
   
# Accessing Values using key name
print(c['a'])

# Accessing values using values()
# method
print(c.values())

# Accessing keys using keys()
# method
print(c.keys())
```

**Output:**
```
1 
ValuesView(ChainMap({‘a’: 1, ‘b’: 2}, {‘c’: 3, ‘d’: 4}, {‘e’: 5, ‘f’: 6})) 
KeysView(ChainMap({‘a’: 1, ‘b’: 2}, {‘c’: 3, ‘d’: 4}, {‘e’: 5, ‘f’: 6}))
```

## Adding new dictionary
A new dictionary can be added by using the `new_child()` method. The newly added dictionary is added at the beginning of the ChainMap.

**Example:**
```Python
import collections 
  
# initializing dictionaries 
dic1 = { 'a' : 1, 'b' : 2 } 
dic2 = { 'b' : 3, 'c' : 4 } 
dic3 = { 'f' : 5 } 
  
# initializing ChainMap 
chain = collections.ChainMap(dic1, dic2) 
  
# printing chainMap 
print ("All the ChainMap contents are : ") 
print (chain) 
  
# using new_child() to add new dictionary 
chain1 = chain.new_child(dic3) 
  
# printing chainMap
print ("Displaying new ChainMap : ") 
print (chain1) 
```

**Output:**
```
All the ChainMap contents are : 
ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
Displaying new ChainMap : 
ChainMap({'f': 5}, {'a': 1, 'b': 2}, {'b': 3, 'c': 4})
```

# Named Tuple
A **NamedTuple** returns a tuple object with names for each position which the ordinary tuples lack. For example, consider a tuple names student where the first element represents fname, second represents lname and the third element represents the DOB. Suppose for calling fname instead of remembering the index position you can actually call the element by using the fname argument, then it will be really easy for accessing tuples element. This functionality is provided by the NamedTuple.

**Example:**
```Python
from collections import namedtuple
  
# Declaring namedtuple() 
Student = namedtuple('Student',['name','age','DOB']) 
  
# Adding values 
S = Student('Nandini','19','2541997') 
  
# Access using index 
print ("The Student age using index is : ",end ="") 
print (S[1]) 
  
# Access using name  
print ("The Student name using keyname is : ",end ="") 
print (S.name)
```

**Output:**
```
The Student age using index is : 19
The Student name using keyname is : Nandini
```

## Conversion Operations 
### `_make():`
This function is used to return a `namedtuple()` from the iterable passed as argument.

### `_asdict():` 
This function returns the `OrdereDict()` as constructed from the mapped values of `namedtuple()`.

**Example:**
```Python
from collections import namedtuple
  
# Declaring namedtuple() 
Student = namedtuple('Student',['name','age','DOB']) 
  
# Adding values 
S = Student('Nandini','19','2541997') 
  
# initializing iterable  
li = ['Manjeet', '19', '411997' ] 
  
# initializing dict 
di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' } 
  
# using _make() to return namedtuple() 
print ("The namedtuple instance using iterable is  : ") 
print (Student._make(li)) 
  
# using _asdict() to return an OrderedDict() 
print ("The OrderedDict instance using namedtuple is  : ") 
print (S._asdict()) 
```

**Output:**
```
The namedtuple instance using iterable is  : 
Student(name='Manjeet', age='19', DOB='411997')
The OrderedDict instance using namedtuple is  : 
OrderedDict([('name', 'Nandini'), ('age', '19'), ('DOB', '2541997')])
```

# Deque
**Deque (Doubly Ended Queue)** is the optimized list for quicker append and pop operations from both sides of the container. It provides `O(1)` time complexity for append and pop operations as compared to list with `O(n)` time complexity.

This function takes the list as an argument.

**Example:**
```Python
from collections import deque
  
# Declaring deque
queue = deque(['name','age','DOB']) 
  
print(queue)
```

**Output:**
```
deque(['name', 'age', 'DOB'])
```

## Inserting Elements
Elements in deque can be inserted from both ends. To insert the elements from right append() method is used and to insert the elements from the left `appendleft()` method is used.

**Example:**
```Python
from collections import deque 
  
# initializing deque 
de = deque([1,2,3]) 
  
# using append() to insert element at right end  
# inserts 4 at the end of deque 
de.append(4) 
  
# printing modified deque 
print ("The deque after appending at right is : ") 
print (de) 
  
# using appendleft() to insert element at right end  
# inserts 6 at the beginning of deque 
de.appendleft(6) 
  
# printing modified deque 
print ("The deque after appending at left is : ") 
print (de) 
```

**Output**
```
The deque after appending at right is : 
deque([1, 2, 3, 4])
The deque after appending at left is : 
deque([6, 1, 2, 3, 4])
```

## Inserting Elements
Elements can also be removed from the deque from both the ends. To remove elements from right use `pop()` method and to remove elements from the left use `popleft()` method.

**Example:**
```Python
from collections import deque

# initializing deque 
de = deque([6, 1, 2, 3, 4])

# using pop() to delete element from right end  
# deletes 4 from the right end of deque 
de.pop() 
  
# printing modified deque 
print ("The deque after deleting from right is : ") 
print (de) 
  
# using popleft() to delete element from left end  
# deletes 6 from the left end of deque 
de.popleft() 
  
# printing modified deque 
print ("The deque after deleting from left is : ") 
print (de) 
```

**Output:**
```
The deque after deleting from right is : 
deque([6, 1, 2, 3])
The deque after deleting from left is : 
deque([1, 2, 3])
```

# UserDict
**UserDict** is a dictionary-like container that acts as a wrapper around the dictionary objects. This container is used when someone wants to create their own dictionary with some modified or new functionality.

**Example:**
```Python
from collections import UserDict 
   
  
# Creating a Dictionary where 
# deletion is not allowed 
class MyDict(UserDict): 
      
    # Function to stop deletion 
    # from dictionary 
    def __del__(self): 
        raise RuntimeError("Deletion not allowed") 
          
    # Function to stop pop from  
    # dictionary 
    def pop(self, s = None): 
        raise RuntimeError("Deletion not allowed") 
          
    # Function to stop popitem  
    # from Dictionary 
    def popitem(self, s = None): 
        raise RuntimeError("Deletion not allowed") 
      
# Driver's code 
d = MyDict({'a':1, 
    'b': 2, 
    'c': 3})
  
d.pop(1)
```

**Output:**
```
Traceback (most recent call last):
  File "/home/f8db849e4cf1e58177983b2b6023c1a3.py", line 32, in <module>
    d.pop(1) 
  File "/home/f8db849e4cf1e58177983b2b6023c1a3.py", line 20, in pop
    raise RuntimeError("Deletion not allowed") 
RuntimeError: Deletion not allowed
Exception ignored in: <bound method MyDict.__del__ of {'a': 1, 'b': 2, 'c': 3}>
Traceback (most recent call last):
  File "/home/f8db849e4cf1e58177983b2b6023c1a3.py", line 15, in __del__
RuntimeError: Deletion not allowed
```

# UserList
**UserList** is a list like container that acts as a wrapper around the list objects. This is useful when someone wants to create their own list with some modified or additional functionality.

**Example:**
```Python
from collections import UserList 
   
  
# Creating a List where 
# deletion is not allowed 
class MyList(UserList): 
      
    # Function to stop deletion 
    # from List 
    def remove(self, s = None): 
        raise RuntimeError("Deletion not allowed") 
          
    # Function to stop pop from  
    # List 
    def pop(self, s = None): 
        raise RuntimeError("Deletion not allowed") 
      
# Driver's code 
L = MyList([1, 2, 3, 4]) 
  
print("Original List") 
  
# Inserting to List" 
L.append(5) 
print("After Insertion") 
print(L) 
  
# Deleting From List 
L.remove() 
```

**Output:**
```
Original List
After Insertion
[1, 2, 3, 4, 5]
```

# UserString
**UserString** is a string like container and just like `UserDict` and `UserList` it acts as a wrapper around string objects. It is used when someone wants to create their own strings with some modified or additional functionality. 

**Example:**
```Python
from collections import UserString 
   
  
# Creating a Mutable String 
class Mystring(UserString): 
      
    # Function to append to 
    # string 
    def append(self, s): 
        self.data += s 
          
    # Function to remove from  
    # string 
    def remove(self, s): 
        self.data = self.data.replace(s, "") 
      
# Driver's code 
s1 = Mystring("Geeks") 
print("Original String:", s1.data) 
  
# Appending to string 
s1.append("s") 
print("String After Appending:", s1.data) 
  
# Removing from string 
s1.remove("e") 
print("String after Removing:", s1.data)
```

**Output:**
```
Original String: Geeks
String After Appending: Geekss
String after Removing: Gkss
```