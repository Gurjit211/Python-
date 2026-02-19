"""

The difference() and difference_update() methods return only items that
are present only in the original set and not in both sets.


"""

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)




cities4 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities5 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities4.difference_update(cities5)
print(cities4)
