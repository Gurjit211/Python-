#The is operator returns True if both variables point to the same object:


# Create two identical lists
list_a = ["apple", "banana"]
list_b = ["apple", "banana"]

# Assign list_a to a new variable name
# This makes list_c the exact same object as list_a
list_c = list_a

# 'is' operator: Returns True if both variables are the same object
print("Are list_a and list_c the same object?", list_a is list_c)

# 'is' operator: returns False because they are separate objects in memory
# even if their contents are equal
print("Are list_a and list_b the same object?", list_a is list_b)

# '==' operator: returns True because the data inside is the same
print("Do list_a and list_b have the same content?", list_a == list_b)

# 'is not' operator: Returns True if both variables are not the same object
print("Are list_a and list_b NOT the same object?", list_a is not list_b)
