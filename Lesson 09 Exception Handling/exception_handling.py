# 1. Basic try-except for input and division
def safe_division():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {result}")
    finally:
        print("Thanks for using the division program.\n")


# 2. Function that raises exception
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


# 3. Custom Exception Class
class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass


# 4. Function using custom exception
def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative number detected!")
    return f"{n} is positive."


# 5. Example: Using NoReturn function
from typing import NoReturn

def terminate_program() -> NoReturn:
    raise SystemExit("Program terminated forcefully!")


# Code Testing (Optional)
if __name__ == "__main__":
    # 1. Basic Exception Handling
    safe_division()

    # 2. Handling function-based exception
    try:
        print(divide(10, 0))
    except ValueError as ve:
        print("Caught an exception:", ve)

    # 3. Handling Custom Exception
    try:
        print(check_positive(-5))
    except NegativeNumberError as ne:
        print("Custom Exception Caught:", ne)

    # 4. NoReturn usage
    try:
        terminate_program()
    except SystemExit as e:
        print("Exit caught:", e)
