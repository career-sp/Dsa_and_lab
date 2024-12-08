'''
Question:
Write a Python program to calculate the distance between two points PQ having 
three coordinates each using the Manhattan distance metric. (Take the points: 
P(1,2,3); Q(2,1,0))
'''
# Coordinates of the points
P = (1, 2, 3)
Q = (2, 1, 0)

# Calculate the Manhattan distance
distance = abs(Q[0] - P[0]) + abs(Q[1] - P[1]) + abs(Q[2] - P[2])

# Display the result
print(f"The Manhattan distance between P{P} and Q{Q} is: {distance}")
