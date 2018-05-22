#!/usr/bin/env python3

# Author: Chris Azzara
# Purpose: Practice using if statements to test user input

ipchk = input("Set IP Address: ")

if ipchk == '192.168.70.1':
    print("The IP Address was set as {}. That is the same as the Gateway, not recommended".format(ipchk))
elif ipchk:
    print("The IP Address was set as {}".format(ipchk))
else:
    print("No IP Address provided")
