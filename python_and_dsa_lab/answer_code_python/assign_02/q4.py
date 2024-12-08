'''
Question:
Try writing a Python program (similar to the previous one) for a three-digit number, 
i.e., if your input is 123, the program should print 321. 
'''

# Input: Take a three-digit number from the user
number = input("Enter a three-digit number: ")

# Ensure the input is valid
if len(number) == 3 and number.isdigit():
    # Reverse the number
    reversed_number = number[::-1]
    print(f"The reversed number is: {reversed_number}")
else:
    print("Invalid input! Please enter a valid three-digit number.")
