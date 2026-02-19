"""
There are three control statements that can be used with for and while loops to alter their behavior.

They are pass, continue, and break.

"""

'''
IndentationError: expected an indented block
To avoid such an error and to continue the code execution, the pass statement is used. The pass statement acts as a placeholder for future code.
'''
"""
i = 1
while (i < 5):
    pass

for j in range(5):
    pass

if (i == 2):
    pass
print("\n")

"""

"""
2. continue:
This keyword is used in loops to end the current iteration and continue to the next iteration of the loop. Sometimes within a loop, we might need to skip a specific iteration.
This can be done using the continue keyword.
"""

for k in range(1, 10):
    if(k % 2 == 0):
        continue   
    print(k)

print("\n") 

""" 3. The break keyword is used to bring the interpreter out of the loop and into the main body of the program.
Whenever the break keyword is used, the loop is terminated, and the interpreter starts executing the next series of statements within the main program.
"""
l = 1
while (l <= 10):
    l = l + 1
    if (l == 5):
        break
    print(l)
print("\n")
