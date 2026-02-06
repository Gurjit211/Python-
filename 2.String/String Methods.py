str1 = "AbcDEfghIJ"
print(str1.upper())

str2 = "AbcDEfghIJ"
print(str2.lower())

# The strip() method removes any white spaces before and after the string.

str3 = " Silver Spoon "
print(str3.strip())

# The rstrip() method removes specified trailing characters (defaults to whitespace).

str4 = "Hello !!!"
print(str4.rstrip("!"))

# The replace() method replaces a string with another string.

str5 = "Silver Spoon"
print(str5.replace("Sp", "M"))

# The split() method splits the given string at the specified instance and returns the separated strings as list items.

str6 = "Silver Spoon"
print(str6.split(" "))  # Splits the string at the whitespace " ".

'''
The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.

The string has no effect if the first character is already uppercase.
'''

str6 = "hello"
capStr6 = str6.capitalize()
print(capStr6)

str7 = "hello WorlD"
capStr7 = str7.capitalize()
print(capStr7)


