cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)


print("\n")


cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

"""
If you want to add more than one item,
simply create another set or any other iterable object (list, tuple, dictionary), and use the update() method to add it into the existing set.
"""
print("\n")
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)


print("\n")

cities.remove("Tokyo")
print(cities)

print("\n")

cities.discard("Delhi")
print(cities)
