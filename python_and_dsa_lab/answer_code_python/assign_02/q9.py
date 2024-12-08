'''
Question:
Write a Python program to calculate the area of a triangle using Heron’s formula. 
Heron's formula is given as: Area of triangle
= (s*(s -a)*(s -b)*(s -c))^(1/2)
where a, b and c are three sides of the triangle and s=(a+b+c)/2.
'''
import math

# Input: Take the sides of the triangle from the user
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Calculate the semi-perimeter (s)
s = (a + b + c) / 2

# Calculate the area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Display the result
print(f"The area of the triangle is: {area:.2f}")
