#!/usr/bin/env python3

# Author : Chris Azzara
# Purpose : Map pollen count to severity level using data input by the user.
#           Uses the chart found at https://www.aaaai.org/global/nab-pollen-counts/reading-the-charts
#           Options are: Mold, Grass, Tree, and Weed pollen

menu = """Pollen Level Script
Select a Type of Pollen (1-4):
              1. MOLD
              2. GRASS
              3. TREE
              4. WEED\n"""
# Prompt user to choose 1-4
choice = input(menu)

if choice == '1':
    print("You've selected MOLD!")
    pcount = int(input("Enter the pollen count: "))
    if pcount >= 50000:
        print("VERY HIGH")
    elif pcount >= 13000 and pcount <= 49999:
        print("HIGH")
    elif pcount >= 6500 and pcount <= 12999:
        print("MODERATE")
    elif pcount >= 1 and pcount <= 6499:
        print("LOW")
    else:
        print("ABSENT")
elif choice == '2':
    print("You've selected GRASS!")
    pcount = int(input("Enter the pollen count: "))
    if pcount >= 200:
        print("VERY HIGH")
    elif pcount >= 20 and pcount <= 199:
        print("HIGH")
    elif pcount >= 5 and pcount <= 19:
        print("MODERATE")
    elif pcount >= 1 and pcount <= 4:
        print("LOW")
    else:
        print("ABSENT")
elif choice == '3':
    print("You've selected TREE!")
    pcount = int(input("Enter the pollen count: "))
    if pcount >= 1500:
        print("VERY HIGH")
    elif pcount >= 90 and pcount <= 1499:
        print("HIGH")
    elif pcount >= 15 and pcount <= 89:
        print("MODERATE")
    elif pcount >= 1 and pcount <= 14:
        print("LOW")
    else:
        print("ABSENT")
elif choice == '4':
    print("You've selected WEED!")
    pcount = int(input("Enter the pollen count: "))
    if pcount >= 500:
        print("VERY HIGH")
    elif pcount >= 50 and pcount <= 499:
        print("HIGH")
    elif pcount >= 10 and pcount <= 49:
        print("MODERATE")
    elif pcount >= 1 and pcount <= 9:
        print("LOW")
    else:
        print("ABSENT")
else:
    print("Invalid Choice...Terminating Script")
