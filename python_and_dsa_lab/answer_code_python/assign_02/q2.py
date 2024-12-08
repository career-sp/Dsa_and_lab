'''
Question:
 Write a Python program that asks a user for a number of years, and then prints out 
the number of days, hours, minutes, and seconds in that number of years. How 
many years?
'''
def calculate_time_in_years(years):
    # Constants
    days_in_year = 365  # Assuming a non-leap year
    hours_in_day = 24
    minutes_in_hour = 60
    seconds_in_minute = 60

    # Calculations
    days = years * days_in_year
    hours = days * hours_in_day
    minutes = hours * minutes_in_hour
    seconds = minutes * seconds_in_minute

    return days, hours, minutes, seconds

# Take input for number of years from the user
try:
    years = int(input("How many years? "))

    if years >= 0:
        days, hours, minutes, seconds = calculate_time_in_years(years)
        print(f"In {years} years, there are:")
        print(f"{days} days")
        print(f"{hours} hours")
        print(f"{minutes} minutes")
        print(f"{seconds} seconds")
    else:
        print("Invalid input. Please enter a non-negative number of years.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")

