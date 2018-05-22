#!/usr/bin/env python3

# Author: Chris Azzara
# Purpose: Make lists of mixed data types and nested lists

list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(list1)

# Print second item in list
print(list1[1])

# Extend the list 
list1.extend(['juniper']) 
print(list1)
# Append a list 
list1.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])
print(list1) # ['cisco_nxos', 'arista_eos', 'cisco_ios, juniper', ['10.1.0.1', '10.2.0.1', '10.3.0.1']]
print(list1[4]) # ['10.1.0.1', '10.2.0.1', '10.3.0.1']
print(list1[4][0]) # 10.1.0.1

list_of_critters = ['Fly', 'Pig', 'Owl', 'Yak', 'Duk']
print(list_of_critters)

