"""
There are four types of arguments that we can provide in a function:

Default Arguments
Keyword Arguments
Required Arguments
Variable-length Arguments
"""
"""Default arguments:
We can provide a default value while creating a function. This way the
function assumes a default value even if a value is not provided in the function call for that argument.
"""

def name(fname, mname = "Shinda", lname = "Sidhu"):
    print("Hello,", fname, mname, lname)

name("Amy")
