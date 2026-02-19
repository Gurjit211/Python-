"""Recursion
We can let the function call itself, such a process is known as calling a function recursively in Python.

"""

def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 5
print("number: ", num)
print("Factorial: ", factorial(num))
