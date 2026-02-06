"""
The replace() method can be used to replace a part of the original string with another string.
"""

str1 = "Python is a Compiled Language."
print(str1.replace("Compiled", "Interpreted"))


"""
The startswith() method checks if the string starts with a given value.
If yes, then return True, else return False
"""

str2 = "Python is a Interpreted Language"
print(str2.startswith("Python"))


"""
The swapcase() method changes the character casing of the string.
Upper case are converted to lower case and lower case to upper case.
"""

str3 = "Python is a Interpreted Language"
print(str3.swapcase())

"""
The title() method capitalizes each letter of the word within the string.
"""
str4 = "He's name is Dan. Dan is an honest man."
print(str4.title())
