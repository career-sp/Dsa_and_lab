'''
Question:
Write a Python program to calculate the distance between two points PQ having 
three coordinates each using the Euclidean distance metric. (Take the points: 
P(1,2,3); Q(2,1,0)).
'''

import math

# Coordinates of the points
P = (1, 2, 3)
Q = (2, 1, 0)

# Calculate the Euclidean distance
distance = math.sqrt((Q[0] - P[0])**2 + (Q[1] - P[1])**2 + (Q[2] - P[2])**2)

# Display the result
print(f"The Euclidean distance between P{P} and Q{Q} is: {distance:.2f}")
