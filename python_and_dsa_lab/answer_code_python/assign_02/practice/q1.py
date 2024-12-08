'''
Question:
Write a Python Program to read Height in Centimetres and then convert the Height to Feet and Inches (Round the result up to 2 places of decimal).

1 centimeter = 0.0328084 feet
1 centimeter = 0.393701 inches
'''
# Input: Take height in centimeters
height_cm = float(input("Enter height in centimeters: "))

# Conversion constants
cm_to_feet = 0.0328084
cm_to_inches = 0.393701

# Convert height to feet
height_feet = height_cm * cm_to_feet

# Extract the integer part of the feet (whole feet)
whole_feet = int(height_feet)

# Convert the fractional part of feet to inches
remaining_inches = (height_feet - whole_feet) * 12

# Round the result to 2 decimal places
remaining_inches = round(remaining_inches, 2)

# Display the result
print(f"Height in feet and inches: {whole_feet} feet and {remaining_inches} inches")
