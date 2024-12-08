'''
Question:
Write a Python program to take a 2-digit number and then print the reversed 
number. That is, if the input given is 25, the program should print 52. 
'''
# Input: Take a 2-digit number from the user
number = input("Enter a 2-digit number: ")

# Ensure the input is valid
if len(number) == 2 and number.isdigit():
    # Reverse the number
    reversed_number = number[::-1]
    print(f"The reversed number is: {reversed_number}")
else:
    print("Invalid input! Please enter a valid 2-digit number.")
