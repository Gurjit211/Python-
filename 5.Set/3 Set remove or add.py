"""pop():
This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered.
However, you can access the popped item if you assign the pop() method to a variable.
"""

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities1.pop()
print(cities1)
print(item)


#del is not a method, rather it is a keyword which deletes the set entirely.
cities2 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities2
print(cities2)


#This method clears all items in the set and prints an empty set.

cities3 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities3.clear()
print(cities3)
