#1 The center() method aligns the string to the center as per the parameters given by the user.

str1 = "Welcome to the Console!!!"
print(str1.center(100))


# We can also provide a padding character. It will fill the rest of the fill characters provided by the user.

str2 = "Welcome to the Console!!!"
print(str2.center(50, "."))


#2  The count() method returns the number of times the given value has occurred within the given string.

str3 = "Abracadabra"
countStr = str3.count("a")
print(countStr)

#3 The endswith() method checks if the string ends with a given value. If yes, then return True, else return False.

str4 = "Welcome to the Console !!!"
print(str4.endswith("!!!"))


''' #4
The find() method searches for the first occurrence of the given value and returns the index where it is present.
If the given value is absent from the string, then return -1.
'''
str5 = "He's name is Dan. He is an honest man."
print(str5.find("is"))

""" 5 The index() method searches for the first occurrence of the given value and returns the index where it is present.
If the given value is absent from the string, then raise an exception."""

str6 = "He's name is Dan. Dan is an honest man."
print(str6.index("Dan"))

""" The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9.
If any other characters or punctuations are present, then it returns False.   """

str7 = "WelcomeToTheConsole"
print(str7.isalnum())

