# trip_planner.py

import math
import calendar
from datetime import datetime, timedelta

def calculate_return_date(start_date: str, days: int) -> str:
    """Calculate the return date after trip duration."""
    start = datetime.strptime(start_date, "%Y-%m-%d")
    return_date = start + timedelta(days=days)
    return return_date.strftime("%Y-%m-%d")

def calculate_total_budget(per_day_budget: float, days: int) -> float:
    """Calculate total budget using math.ceil to round up the value."""
    total = per_day_budget * days
    return math.ceil(total)

def show_month_calendar(year: int, month: int):
    """Print calendar for the travel month."""
    print("\n📅 Travel Month Calendar:")
    print(calendar.month(year, month))

# Main program
if __name__ == "__main__":
    print("✈️  Welcome to Trip Planner!\n")

    try:
        # Inputs
        start_date = input("📅 Enter your trip start date (YYYY-MM-DD): ")
        days = int(input("📆 How many days will you travel?: "))
        per_day_budget = float(input("💰 Enter your estimated daily budget (Rs): "))

        # Validations
        if days <= 0:
            raise ValueError("Days must be greater than 0.")
        if per_day_budget <= 0:
            raise ValueError("Budget must be greater than 0.")

        # Calculations
        return_date = calculate_return_date(start_date, days)
        total_budget = calculate_total_budget(per_day_budget, days)
        start_obj = datetime.strptime(start_date, "%Y-%m-%d")

        # Output
        print(f"\n🗓 Your trip will end on: {return_date}")
        print(f"💸 Total estimated budget: Rs. {total_budget}")

        # Show calendar of trip month
        show_month_calendar(start_obj.year, start_obj.month)

    except ValueError as ve:
        print(f"❌ Input Error: {ve}")
    except Exception as e:
        print(f"⚠️ Something went wrong: {e}")
    finally:
        print("\n✅ Thank you for using Trip Planner!")
