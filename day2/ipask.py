#!/usr/bin/env python3

# Author: Chris Azzara
# Purpose: Ask user for IP and MAC address and display it back to them

# Collect User Input
ip = input("Enter your IP Address: ")
mac = input("Enter your MAC Address: ")

# Display Info
print("Your IP Address is {} and your MAC Address is {}".format(ip, mac))
octets = ip.split(".")
octets = map(int, octets)
print("Your IP Address in Hex: {:02X}{:02X}{:02X}{:02X}".format(*octets))
