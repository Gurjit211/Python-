'''
Mutable Data Types
Mutable means changeable. If a data type is mutable, it means you can add, remove, or modify its elements without creating a new object in memory. When you change a mutable object, its memory address (ID) stays the same.
'''
""" Common mutable data types:

list
dict
set
bytearray
"""
# Example of a mutable data type (list)
fruits = ["apple", "banana", "cherry"]
print(id(fruits))  # Memory address before modification

fruits.append("mango")  # Adding a new item
print(fruits)
print(id(fruits))  # Same memory address → same object

"""Immutable Data Types
mmutable means unchangeable. If a data type is immutable, it means its value cannot be changed once created.
"""

'''
Common immutable data types:

int
float
complex
str
tuple
bool
bytes

'''

# Example of an immutable data type (string)
name = "Harry"
print(id(name))  # Memory address before modification

name = name + " Potter"  # Concatenating creates a new string
print(name)
print(id(name))  # Different memory address → new object created




