''' 
Question:
Write a Python program to take two inputs for day, month and then calculate which 
day of the year, the given date is. For simplicity take 30 days for all months. For 
example, if you give input as: Day 3, Month: 2, then it should print “Day of the 
year: 33”. 
'''
def calculate_day_of_year(day, month):
    # Calculate the day of the year assuming each month has 30 days
    day_of_year = (month - 1) * 30 + day
    return day_of_year

# Take inputs for day and month from the user
try:
    day = int(input("Enter the day (1-30): "))
    month = int(input("Enter the month (1-12): "))

    # Validate the inputs
    if 1 <= day <= 30 and 1 <= month <= 12:
        result = calculate_day_of_year(day, month)
        print(f"Day of the year: {result}")
    else:
        print("Invalid input. Please ensure day is between 1-30 and month is between 1-12.")
except ValueError:
    print("Invalid input. Please enter numeric values.")
