def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")

def print_upto_n(n):
    print("Printing numbers from 1 to", n)
    for i in range(1, n + 1):
        print(i)

def countdown(start):
    print("Countdown:")
    while start > 0:
        print(start)
        start -= 1
    print("Time's up!")

def skip_even_upto_n(n):
    print("Printing only odd numbers up to", n)
    for i in range(1, n + 1):
        if i % 2 == 0:
            continue
        print(i)

def stop_on_7(n):
    print("Stop when 7 is found")
    for i in range(1, n + 1):
        if i == 7:
            print("Found 7! Breaking the loop.")
            break
        print(i)

print(check_even_odd(10))
print(print_upto_n(5))
print(countdown(5))
print(skip_even_upto_n(10))
print(stop_on_7(10))