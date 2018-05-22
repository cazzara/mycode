#!/usr/bin/env python3

# Author: Chris Azzara
# Purpose: Use conditionals to check if a user input is correct

# Collect user input
hostname = input('Enter the hostname of the machine: ')

# Transform user input to uppercase and test against MTG
if hostname.upper() == 'MTG':
    print('hostname matches expected config') # if True, print message

# Exit message displays regardless 
print('Exiting the script...')

