"""Variable names can only contain alphanumeric characters and underscores (A-Z, 0-9, and _).
Variable names must start with a letter or the underscore character.
Variables are case sensitive.
Variable names cannot start with a number."""

name = "Gurjit"   # type str
age = 30            # type int
passed = True       # type bool

print(name, age, passed)

icecream = "Vanilla"    # global variable
def foods():
    vegetable = "Potato"    # local variable
    fruit = "Lichi"         # local variable
    print(vegetable + " is a local variable value.")
    print(icecream + " is a global variable value.")
    print(fruit + " is a local variable value.")

foods() # calling function

