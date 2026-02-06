# Membership operators are used to test if a sequence is presented in an object:

# --- Membership Operators Demo ---

# Membership in Lists
# Using 'inventory' instead of 'fruits'
inventory = ["apple", "banana", "cherry"]

# in: Returns True if a sequence with the specified value is present in the object
print("Is banana in inventory?", "banana" in inventory)

# not in: Returns True if a sequence with the specified value is not present in the object
print("Is pineapple not in inventory?", "pineapple" not in inventory)


# Membership in Strings
# Using 'greeting' instead of 'text'
greeting = "Hello World"

# Checking for specific characters or substrings
print("Is 'H' in greeting?", "H" in greeting)
print("Is 'hello' in greeting?", "hello" in greeting) # Note: This is False because of case sensitivity
print("Is 'z' not in greeting?", "z" not in greeting)
