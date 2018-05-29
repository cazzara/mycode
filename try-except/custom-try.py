#!/usr/bin/env python3

menu = """
Select an exception to raise: 

(1) - StopIteration
(2) - ArithmeticError
(3) - AssertionError
(4) - AttributeError
(5) - EOFError
(6) - ImportError
(7) - KeyboardInterrupt
(8) - LookupError
(9) - IndexError
"""
err_dict = {'1': StopIteration, '2': ArithmeticError, '3': AssertionError, '4': AttributeError, '5': EOFError, '6': ImportError, '7': KeyboardInterrupt, '8': LookupError, '9': IndexError}
choice = input(menu)

try:
    err = err_dict[choice]
except KeyError:
    print("Invalid Selection...")
else:
    raise err
finally:
    print("And that's how you handle errors")
