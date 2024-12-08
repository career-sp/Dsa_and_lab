'''
Question:
 i) Write a Python program to convert degrees Celsius to degrees Fahrenheit.
ii) Write a Python program to convert degrees Fahrenheit to degrees Celsius.
'''
# Celsius to Fahrenheit conversion
celsius = float(input("Enter temperature in degrees Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

# Fahrenheit to Celsius conversion
fahrenheit = float(input("Enter temperature in degrees Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
