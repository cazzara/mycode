#!/usr/bin/env python3

# Author : Chris Azzara
# Purpose : Prompt user to enter a protocol and determine whether or not it is allowed
#           [eth|otn] are ok    [fc|ifb] are not ok 
#           No other protocols are recognized

while True:
    proto = input("Enter a Layer 2 network protocol\n")
    proto = proto.lower()
    if proto == 'eth':
        print("Ethernet protocol allowed")
        break
    elif proto == 'fc':
        print("Fibre Channel NOT allowed")
        break
    elif proto == 'ifb':
        print("Infiniband NOT allowed")
        break
    elif proto == 'otn':
        print("Optical Network allowed")
        break
    else:
        print("No idea what {} is...".format(proto))
