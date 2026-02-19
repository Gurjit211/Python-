"""
In case we don’t pass the arguments with a key = value syntax,
then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with the actual function definition.

"""

def name(fname, mname, lname):
    print("Hello,\t", fname, mname, lname)

name("Gurjit", "Singh", "Sidhu")
