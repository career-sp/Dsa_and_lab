'''
Question:
Write a Python program to swap two numbers using a temporary variable.
'''
# Input: Take two numbers from the user
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

# Swap using a temporary variable
temp = x
x = y
y = temp

# Display the swapped numbers
print(f"After swapping: x = {x}, y = {y}")
