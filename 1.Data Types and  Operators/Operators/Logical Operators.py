# Logical operators are used to combine conditional statements:


# --- Logical Operators Demo ---

# Initializing the variable
score = 3

# 1. 'and' operator 
# Returns True if both statements are true
print("Is score < 5 and score < 10?", score < 5 and score < 10)

# 2. 'or' operator
# Returns True if at least one statement is true
print("Is score < 5 or score < 2?", score < 5 or score < 2)

# 3. 'not' operator
# Reverses the result (True becomes False, and vice versa)
print("The reverse of (score < 5 and score < 10) is:", not(score < 5 and score < 10))
