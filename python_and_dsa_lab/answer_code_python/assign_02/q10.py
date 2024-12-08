'''
Question:
Write a Python program to swap two numbers without using a temporary variable. 
'''
# Input: Take two numbers from the user.
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

# Swapping without using a temporary variable.
x, y = y, x

# Display the swapped numbers.
print(f"After swapping: x = {x}, y = {y}")
