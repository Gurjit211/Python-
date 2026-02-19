"""
Python Set Methods: Comparison Reference
----------------------------------------
1. isdisjoint(): Do we share nothing? ("We are complete strangers.")
2. issuperset(): Do I contain everything you have? ("I am the parent/container.")
3. issubset():   Is everything I have inside you? ("I am a part of you.")
"""

# Base data for examples
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
asia_cities = {"Tokyo", "Delhi"}
mixed_cities = {"Tokyo", "Seoul", "Kabul"}
remote_cities = {"Seoul", "Kabul"}

# --- 1. isdisjoint() ---
# Checks if two sets have NO elements in common.
print("--- isdisjoint() ---")
print(cities.isdisjoint(remote_cities))  # True: No matches
print(cities.isdisjoint(mixed_cities))   # False: Tokyo is in both


# --- 2. issuperset() ---
# Checks if the first set contains everything in the second set.
print("\n--- issuperset() ---")
print(cities.issuperset(asia_cities))    # True: Tokyo/Delhi are in 'cities'
print(cities.issuperset(mixed_cities))   # False: Seoul/Kabul are missing


# --- 3. issubset() ---
# Checks if the current set is entirely contained within the other.
print("\n--- issubset() ---")
print(asia_cities.issubset(cities))      # True: Every element is in 'cities'
print(mixed_cities.issubset(cities))     # False: Seoul/Kabul are not in 'cities'


# Quick Comparison Table (Reference)
"""
| Method         | Logic                        | Analogy                     |
| :------------- | :--------------------------- | :-------------------------- |
| isdisjoint()   | Do we share nothing?         | "We are complete strangers."|
| issuperset()   | Do I contain everything?     | "I am the parent."          |
| issubset()     | Is everything I have in you? | "I am a part of you."       |
"""
