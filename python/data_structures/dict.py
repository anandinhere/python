print(f'''

enumerate(my_dict.items())

Python has a set of built-in methods that you can use on dictionaries.

Python dictionaries do not have a remove() method like lists do. Instead, there are several ways to remove items (key-value pairs) from a dictionary:


Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
        1. Shallow Copy using dict.copy():
        The copy() method creates a new dictionary that contains the same key-value pairs as the original. 
        However, if the dictionary contains mutable objects (like lists or other dictionaries) as values, 
        these nested objects are still references to the same objects in memory. 
        Modifying a nested mutable object in the copy will also affect the original.

2. Deep Copy using copy.deepcopy():
        For a completely independent copy, including all nested mutable objects, 
        the deepcopy() function from the copy module should be used. 
        This creates new copies of all objects, ensuring that changes 
        to the deep copy do not affect the original dictionary or any of its nested structures.
        Python
        
        import copy
        
        original_dict = {{'a': 1, 'b': [2, 3]}}
        deep_copy_dict = copy.deepcopy(original_dict)
        
        deep_copy_dict['a'] = 100
        deep_copy_dict['b'].append(4)
        
        print(original_dict)  # Output: {{'a': 1, 'b': [2, 3]}}
        print(deep_copy_dict) # Output: {{'a': 100, 'b': [2, 3, 4]}}

fromkeys()	Create a dictionary with keys from an iterable and a default value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. 
                If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs, Merge two dictionaries using update()
values()	Returns a list of all the values in the dictionary


enumerate() and .items() are two different tools in Python, and they are often used together when iterating over a dictionary. The choice between using them separately or combined depends on whether you need a loop counter or just the key-value pairs. 
dict.items()
The .items() method is the standard and most Pythonic way to iterate over a dictionary to access both its keys and values. 
Returns: A "view object" that displays a list of the dictionary's (key, value) tuples.
Best for: When you only need access to the key and value of each item and do not need a numeric index for the iteration. 
Example
python
my_dict = {{"apple": 1, "banana": 2, "cherry": 3}}

for key, value in my_dict.items():
    print(f"Key: {{key}}, Value: {{value}}")

# Output:
# Key: apple, Value: 1
# Key: banana, Value: 2
# Key: cherry, Value: 3
Use code with caution.

enumerate()
The built-in enumerate() function adds a counter to any iterable, including lists, tuples, or even a dictionary. By default, it returns a sequence of (index, item) tuples. 
Behavior with a dictionary: When used directly on a dictionary, enumerate() iterates only over the dictionary's keys and provides an index for each key. This is generally not the intended behavior if you want the values as well.
Best for: When you need a numeric index in addition to iterating over the items of an iterable. 
Example (with a dictionary)
python
my_dict = {{"apple": 1, "banana": 2, "cherry": 3/}}

for index, key in enumerate(my_dict):
    print(f"Index: {{index}},Key: {{key}}")

# Output:
# Index: 0, Key: apple
# Index: 1, Key: banana
# Index: 2, Key: cherry
Use code with caution.

Combining enumerate() and .items()
To get an index along with both the key and the value, you can pass the results of my_dict.items() into the enumerate() function. This is a common and powerful pattern for iterating over dictionaries. 
Returns: A sequence of (index, (key, value)) tuples, which can be unpacked in the loop.
Best for: When you need a loop counter in addition to the key-value pairs. 
Example
python
my_dict = {{"apple": 1, "banana": 2, "cherry": 3/}}

for index, (key, value) in enumerate(my_dict.items()):
    print(f"Index: {{index}}, Key: {{key}}, Value: {{value}}")

# Output:
# Index: 0, Key: apple, Value: 1
# Index: 1, Key: banana, Value: 2
# Index: 2, Key: cherry, Value: 3

''')


print(f'''
Dictionary is one of the built-in datatype that allows us to store data 
in key-value pair which is unordered and mutable.


''')


print(f'''


1. Creating a Dictionary: Create a dictionary using curly braces
Example: my_dict = {{"key1": "value1", "key2": "value2"}}

''')


my_dict = {"key1": "value1", "key2": "value2"}

print(f'''
2. Creating an Empty Dictionary: Create an empty dictionary
Example: empty_dict = {{}}


''')

empty_dict = {}


print(f'''
3. Accessing Values: Get a value by its key
Example: value = my_dict["key1"] → value is "value1"

''')

value = my_dict["key1"]
print(value)

print(f'''
4. Adding or Updating Values: Add a new key-value pair or update an existing key
Example: my_dict["key3"] = "value3" → my_dict becomes 
{{"key1": "value1", "key2": "value2", "key3": "value3"}}


''')

my_dict["key3"] = "value3"
print(my_dict)

print(f'''
5. Removing a Key-Value Pair: Remove a key-value pair using del
Example: del my_dict["key2"] → my_dict becomes {{"key1": "value1", "key3": "value3"}}

''')

del my_dict["key1"]
print(my_dict)

print(f'''
6. Popping a Key-Value Pair: Remove and return a value using pop()
Example: value = my_dict.pop("key1") → my_dict becomes {{"key3": "value3"}}


''')

value = my_dict.pop("key3")
print(value)
print(my_dict)


print(f'''
7. Clearing a Dictionary: Remove all key-value pairs using clear()
Example: my_dict.clear() → my_dict becomes {{}}

''')

my_dict.clear()
print(my_dict)

print(f'''
8. Checking for a Key: Check if a key exists using in
Example: exists = "key1" in my_dict → exists is True

9. Getting the Length: Get the number of key-value pairs using len()
Example: length = len(my_dict) → length is the count of pairs

10. Getting Keys: Get all keys using keys()
Example: keys = my_dict.keys() → keys is a view of all keys
   Dynamically updated
If you modify the original dictionary, the view object will automatically reflect the change. 
A list created from the keys will not. 

11. Getting Values: Get all values using values()
Example: values = my_dict.values() → values is a view of all values

12. Getting Items: Get all key-value pairs using items()
Example: items = my_dict.items() → items is a view of all key-value pairs



''')


my_dict = {"key1": "value1", "key2": "value2"}

keys = my_dict.keys()
print(list(keys))
vals = my_dict.values()
print(vals)

items = my_dict.items()
print(items)


print(f'''
13. Copying a Dictionary: Create a shallow copy using copy()
Example: my_dict_copy = my_dict.copy() → my_dict_copy is a new dictionary with the same items

14. Merging Dictionaries: Merge two dictionaries using update()
Example: my_dict.update({{"key4": "value4"}}) → adds key4 to my_dict


''')
my_dict_copy = my_dict.copy()
print(my_dict_copy)

print(f'''
15. Dictionary Comprehension: Create a dictionary using a comprehension
Example: squared_dict = {{x: x**2 for x in range(5)}} → squared_dict is {{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}}



''')

my_dict_comp = {x:x*x for x in range(0,10)}
print(my_dict_comp)

print(f'''
16. Nested Dictionaries: Dictionaries can contain other dictionaries
Example: nested_dict = {{"outer": {{"inner": "value"}}}} → Accessing: nested_dict["outer"]["inner"] → "value"


''')

nested_dict = {"outer" : {"inner":"value"}}
print(nested_dict["outer"]["inner"])

print(f'''
17. Default Values: Use get() to return a value with a default if the key is not found
Example: value = my_dict.get("key5", "default") → value is "default"


''')

val = my_dict.get("key69","69")
print(val)

print(f'''
18. Popitem: Remove and return the last inserted key-value pair using popitem()
Example: last_item = my_dict.popitem() → my_dict is modified


''')

last_item = my_dict.popitem()
print(last_item)



print(f'''
19. Dictionary from Keys: Create a dictionary with keys from an iterable and a default value
Example: new_dict = dict.fromkeys(["a", "b", "c"], 0) → new_dict is {{"a": 0, "b": 0, "c": 0}}



''')
new_dict = dict.fromkeys(["a", "b", "c"], 0)
print(new_dict)


print(f'''
20. Updating Multiple Keys: Update multiple key-value pairs at once
Example: my_dict.update({{"key1": "new_value", "key3": "new_value"}}) → updates specified keys

21. Iterating Over Keys :Loop through keys in a dictionary
Example: for key in my_dict: print(key)

22. Iterating Over Values: Loop through values in a dictionary
Example: for value in my_dict.values(): print(value)


''')

print(my_dict)
my_dict.update({"key1": "new_value", "key3": "new_value"})
print(my_dict)

print(f'''
23. Iterating Over Items: Loop through key-value pairs in a dictionary
Example: for key, value in my_dict.items(): print(key, value)


''')

for key, value in my_dict.items(): print(key, value)


print(f'''
24. Finding Key Index: Use next() with an iterator to find the index of a key
Example: index = next((i for i, k in enumerate(my_dict) if k == “key1”), None)

''')

index = next((i for i, k in enumerate(my_dict) if k == "key12"), None)
print(index)

print(f'''
25. Converting to List: Convert keys, values, or items to a list
Example: keys_list = list(my_dict.keys()) → keys_list contains the keys of my_dict


''')

keys_list = list(my_dict.keys())
print(keys_list)