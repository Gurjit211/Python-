cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# The symmetric_difference() and symmetric_difference_update() methods return only items that are not similar to both sets.


cities.symmetric_difference_update(cities2)
print(cities)
