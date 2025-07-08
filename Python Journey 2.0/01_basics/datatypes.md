# Object types / Data types in Python

- **Numbers :** 1234, 3.14, 0b1010, 0o12, 0x1A
- **Strings :** "Hello, World!", 'Python', """Triple quotes""", '''Single triple quotes'''
- **Lists :** [1, 2, 3], ['a', 'b', 'c'], [1, 'two', 3.0]
- **Tuples :** (1, 2, 3), ('a', 'b', 'c'), (1, 'two', 3.0)
- **Sets :** {1, 2, 3}, {'a', 'b', 'c'}, {1, 'two', 3.0}
- **Dictionaries :** {'key1': 'value1', 'key2': 'value2'}, {1: 'one', 2: 'two'}, {'name': 'Alice', 'age': 30}
- **Booleans :** True, False
- **None :** None
- **files :** open('file.txt', 'r'), open('data.csv', 'w')
- **Another data types:** functions, modules, classes

**What is a data type?**
A data type is a classification that specifies which type of value a variable can hold. 

**Sets:** Sets are unordered collections of unique elements. They are defined using curly braces `{}` or the `set()` constructor. Sets are useful for membership testing and eliminating duplicate entries.
Example:
```python       
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5}
```

**Dictionaries:** Dictionaries are collections of key-value pairs. They are defined using curly braces `{}` with keys and values separated by colons. Dictionaries are useful for storing data that is associated with a unique key.
Example:    
```python
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
my_dict['age'] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}
my_dict['country'] = 'USA'
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}
my_dict.pop('city')
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}
```

**Tuples:** Tuples are ordered collections of elements that are immutable (cannot be changed after creation). They are defined using parentheses `()`. Tuples are useful for grouping related data together.
Example:
```python
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)
my_tuple = (1, 2, 3, 4)
print(my_tuple)  # Output: (1, 2, 3, 4)
my_tuple = (1, 'two', 3.0)
print(my_tuple)  # Output: (1, 'two', 3.0)
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)
```
**Lists:** Lists are ordered collections of elements that are mutable (can be changed after creation). They are defined using square brackets `[]`. Lists are useful for storing a sequence of items.
Example:
```python
my_list = [1, 2, 3]
print(my_list)  # Output: [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
my_list[1] = 'two'
print(my_list)  # Output: [1, 'two', 3, 4]
my_list.remove(3)
print(my_list)  # Output: [1, 'two', 4]
my_list.sort()
print(my_list)  # Output: [1, 'two', 4]

