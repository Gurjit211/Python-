# Bitwise operators are used to compare (binary) numbers:

# --- Python Bitwise Operators Demo ---

# Variables (Binary equivalents for understanding)
# first_val  = 10  (Binary: 1010)
# second_val = 4   (Binary: 0100)
first_val = 10
second_val = 4

# 1. & (Bitwise AND)
# Result is 1 only if both bits are 1
print("Bitwise AND (10 & 4):", first_val & second_val)

# 2. | (Bitwise OR)
# Result is 1 if at least one bit is 1
print("Bitwise OR (10 | 4):", first_val | second_val)

# 3. ^ (Bitwise XOR)
# Result is 1 if bits are different
print("Bitwise XOR (10 ^ 4):", first_val ^ second_val)

# 4. ~ (Bitwise NOT)
# Inverts all the bits (Formula: ~x = -(x + 1))
print("Bitwise NOT (~10):", ~first_val)

# 5. << (Zero fill left shift)
# Shifts bits to the left, pushing in zeros from the right
# (Effectively multiplies by 2 for each shift)
print("Left Shift (10 << 2):", first_val << 2)

# 6. >> (Signed right shift)
# Shifts bits to the right
# (Effectively divides by 2 for each shift)
print("Right Shift (10 >> 2):", first_val >> 2)
