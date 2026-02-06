# --- Python Assignment Operators Demo ---

# 1. Basic Assignment (=)
total = 10
print("Assignment: total =", total)

# 2. Addition Assignment (+=)
score = 20
score += 5  
print("Addition: score is now", score)

# 3. Subtraction Assignment (-=)
balance = 100
balance -= 20  
print("Subtraction: balance is now", balance)

# 4. Multiplication Assignment (*=)
factor = 4
factor *= 3  
print("Multiplication: factor is now", factor)

# 5. Division Assignment (/=)
ratio = 10
ratio /= 2  
print("Division: ratio is now", ratio)

# 6. Modulus Assignment (%=)
remainder = 10
remainder %= 3  
print("Modulus: remainder is now", remainder)

# 7. Floor Division Assignment (//=)
level = 11
level //= 3  
print("Floor Division: level is now", level)

# 8. Exponentiation Assignment (**=)
power = 2
power **= 3  
print("Exponentiation: power is now", power)

# --- Bitwise Assignment Operators ---

# 9. Bitwise AND Assignment (&=)
mask = 6      
mask &= 3     
print("Bitwise AND: mask is now", mask)

# 10. Bitwise OR Assignment (|=)
flags = 4     
flags |= 2    
print("Bitwise OR: flags is now", flags)

# 11. Bitwise XOR Assignment (^=)
toggle = 5    
toggle ^= 3   
print("Bitwise XOR: toggle is now", toggle)

# 12. Right Shift Assignment (>>=)
pixels = 16   
pixels >>= 2  
print("Right Shift: pixels is now", pixels)

# 13. Left Shift Assignment (<<=)
data = 1      
data <<= 3    
print("Left Shift: data is now", data)

# 14. Walrus Operator (:=)
# Assigns 50 to 'value' and prints it immediately
print("Walrus Assignment: value is", (value := 50))
