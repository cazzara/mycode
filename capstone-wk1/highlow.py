# -*- coding: utf-8 -*-
"""
Author : Chris Azzara
Purpose : A simple number guessing game. This program will try to guess a secret number between 1 - 100 
          The user will enter whether the guess is too high or too low or correct. The program uses the binary search algorithm to narrow the search space.
"""

print("Number Guessing Game!")
print("Think of a number between 1 and 100 and I will try to guess it!")

high = 100
low = 1
mid = (high + low) // 2

while low <= high:
    print("Is the number you are thinking of {}?".format(mid))
    print("high {} mid {} low {}".format(high, mid, low))
    response = input("y = yes\nh = too high\nl = too low\n")
    
    if response[0].lower() == 'y':
        print("Aha! I knew it!")
        break
    elif response[0].lower() == 'h':
        high = mid - 1
        mid = (high + low) // 2
    elif response[0].lower() == 'l':
        low = mid + 1
        mid = (high + low) // 2
    else:
        print("Sorry I didn't understand that...Let's try again")

