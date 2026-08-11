import sys

# Check if a year argument was provided
if len(sys.argv) < 2:
    print("Error: Please provide a year. Example: python leap_year.py 2024")
    sys.exit(1)

try:
    year = int(sys.argv[1])
except ValueError:
    print("Error: Year must be an integer.")
    sys.exit(1)

# Leap year logic
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
