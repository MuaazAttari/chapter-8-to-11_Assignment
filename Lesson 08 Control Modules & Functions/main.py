# main.py

import control_modules as cm
import functions as fn

# Control Module Tests
cm.check_even_odd(7)
cm.print_upto_n(5)
cm.countdown(3)
cm.skip_even_upto_n(10)
cm.stop_on_7(10)

# Functions Module Tests
print(fn.greet("Muaaz"))
print("Addition:", fn.add_numbers(5, 3))
print("Multiplication:", fn.multiply_numbers(4, 2))
print("Division:", fn.divide_numbers(10, 0))
print("Maximum:", fn.get_maximum(3, 9, 5))
print(fn.print_details("Muaaz", 22))
