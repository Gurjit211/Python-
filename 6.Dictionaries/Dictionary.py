info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

"""

1. Accessing Single Values:
Values in a dictionary can be accessed using keys.
We can access dictionary values by mentioning keys either in square brackets or by using the get method.

"""
print("\n")
print(info['name'])
print(info.get('eligible'))

# 2. Accessing Multiple Values:
print("\n")
print(info.values())

# 3 Accessing Keys:
print("\n")
print(info.keys())

#4Accessing Key-Value Pairs:

print(info.items())
