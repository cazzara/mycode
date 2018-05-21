#!/usr/bin/env python3
# Author: Chris Azzara
# Collect input from user (IP) and display it back to them

# Collect Info From User
user_input = input("Please input an IPv4 address: ")
vendor = input("Enter vendor information: ")

# Display Info to User
print("The IP address given is {}".format(user_input))
print("The vendor is {}".format(vendor))
