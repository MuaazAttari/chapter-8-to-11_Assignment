def greet(name):
    return f"Hello, {name}! How are you?"

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def get_maximum(a, b, c):
    return max(a, b, c)

def print_details(name, age, city="Hyderabad"):
    return f"{name} is {age} years old and lives in {city}."

print(greet("Ali"))
print(add_numbers(5, 10))
print(multiply_numbers(5, 10))
print(divide_numbers(10, 2))
print(get_maximum(5, 10, 15))
print(print_details("Muaaz", 22, "Hyderabad"))