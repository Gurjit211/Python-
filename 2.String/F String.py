'''
In Python, f-Strings are used for string formatting. Introduced in Python 3.6, they allow you
to embed variables and expressions directly inside a string using curly braces {}.
'''

name = "Tony"
age = 35
print(f"My name is {name} and I am {age} years old.")

'''
Why use f-Strings?
Before f-Strings, string concatenation or the format() method was used to combine strings and variables.
f-Strings make this process simpler and more readable.

'''
#Example 1: Using concatenation
name1 = "Tony"
age1 = 35
print("My name is " + name1 + " and I am " + str(age1) + " years old.")

#Example 2: Using format()

name2 = "Tony"
age2 = 35
print("My name is {} and I am {} years old.".format(name2, age2))

# Example 3: Using f-String
name3 = "Tony"
age3 = 35
print(f"My name is {name3} and I am {age3} years old.")


#Formatting Numbers
pi = 3.1415926535
print(f"Value of pi: {pi:.2f}")

