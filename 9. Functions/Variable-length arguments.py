"""

Sometimes we may need to pass more arguments than those defined in the actual function.
This can be done using variable-length arguments.

"""


"""
Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function.
The function accesses the arguments by processing them in the form of a tuple.
"""
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("Gurjit", "Singh", "Sidhu")
