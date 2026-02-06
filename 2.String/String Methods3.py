
'''
The isalpha() method returns True only if the entire string only consists of A-Z, a-z.
If any other characters or punctuations or numbers (0-9) are present, then it returns False.
'''
str1 = "Welcome"
print(str1.isalpha())

str2 = "hello world"
print(str2.islower())


"""
The isprintable() method returns True if all the values within the given string are printable,
if not, then return False.
"""

str3 = "We wish you a Merry Christmas"
print(str3.isprintable())

"""
The isspace() method returns True only and only if the string contains white spaces, else returns False.
"""

str4 = "  "  # using Spacebar
print(str4.isspace())
str5 = "        "  # using Tab
print(str5.isspace())

''' The istitle() returns True only if the first letter of each word of the string is capitalized, else it returns False.
'''

str6 = "World Health Organization"
print(str6.istitle())

"""
The isupper() method returns True if all the characters in the string are upper case, else it returns False.
"""
str7 = "WORLD HEALTH ORGANIZATION"
print(str7.isupper())
