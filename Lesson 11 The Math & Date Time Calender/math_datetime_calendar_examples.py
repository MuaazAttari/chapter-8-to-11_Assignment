import math
from datetime import datetime, timedelta
import calendar

# ======= MATH MODULE EXAMPLES =======

print("🔢 MATH MODULE EXAMPLES:")

x = 5.7
print(f"math.floor({x}) =>", math.floor(x))  # 5
print(f"math.ceil({x}) =>", math.ceil(x))    # 6
print(f"math.sqrt(25) =>", math.sqrt(25))    # 5.0
print(f"math.pow(2, 3) =>", math.pow(2, 3))   # 8.0
print(f"math.factorial(5) =>", math.factorial(5))  # 120
print(f"math.pi =>", math.pi)                # 3.141592...

# ======= DATETIME MODULE EXAMPLES =======

print("\n📅 DATETIME MODULE EXAMPLES:")

now = datetime.now()
print("Current Date & Time:", now)

today = datetime.today()
print("Today:", today.date())

# Add 7 days to current date
future = now + timedelta(days=7)
print("7 days later:", future.date())

# Custom date format
custom_date = datetime.strptime("2025-04-20", "%Y-%m-%d")
print("Custom Parsed Date:", custom_date.date())

# Format current datetime
formatted = now.strftime("%A, %d %B %Y, %I:%M %p")
print("Formatted Date:", formatted)

# ======= CALENDAR MODULE EXAMPLES =======

print("\n🗓 CALENDAR MODULE EXAMPLES:")

# Check if year is leap
year = 2024
print(f"Is {year} a leap year? =>", calendar.isleap(year))

# Number of leap years between two years
print("Leap years from 2000 to 2025 =>", calendar.leapdays(2000, 2025))

# Print a whole month calendar
print("\nCalendar for April 2025:")
print(calendar.month(2025, 4))

# Print full year calendar
# print(calendar.calendar(2025))  # (Uncomment if you want full year calendar)
