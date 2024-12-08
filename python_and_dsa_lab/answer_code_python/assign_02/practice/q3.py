'''
Qustion:
Write a Python program to compute (a + b)^3 using the formula 
a^3 + b^3 + 3a^2b + 3ab^2
'''
# Input: Take two numbers (a and b) from the user
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

# Compute using the formula a^3 + b^3 + 3a^2b + 3ab^2
result = a**3 + b**3 + 3 * a**2 * b + 3 * a * b**2

# Display the result
print(f"The result of (a + b)^3 is: {result}")
