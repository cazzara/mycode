#!/usr/bin/env python3

# Author : Chris Azzara
# Purpose : Repeatedly ask user to input an IP address and add it to a list. 
#           If the user enters in 10.10.3.1 or 10.20.5.2, warn user not to use this IP
#           If the user enters a 'q', exit the loop and display the list of IP Addresses
# This script assumes the user will enter a valid IPv4 address

# Prompt to display to user
menu = "Enter in an IP Address or type 'q' to quit!\n"

ip_addrs = [] 
choice = '' # choice is initially empty

while choice.lower() != 'q': # As long as 'choice' isn't 'q' the loop will continue
    choice = input(menu) 
    if choice == '10.10.3.1':
        print("Error: That is the Gateway's IP address")
    elif choice == '10.20.5.2':
        print("Error: That is the DNS server's IP address")
    elif choice != 'q': # We don't want the 'q' to be appended to the list
        ip_addrs.append(choice)
    else:
        print("Here is the list of IPs: ")
        print(ip_addrs)
        print("Script Exiting...")
