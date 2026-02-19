'''The union() and update() methods return all items that are present in either of the two sets.
The union() method returns a new set,
whereas the update() method adds items into the existing set from another set.

'''

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.union(cities2)
print(cities3)




cities4 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities5 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities4.intersection_update(cities5)
print(cities4)



