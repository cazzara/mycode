#!/usr/bin/env python3
# Author: Chris Azzara
# Purpose: Practice manipulating the print function parameters

print("O", sep="", end="") 
print("R", sep="", end="")
print("A", sep="", end="")
print("N", sep="", end="")
print("G", sep="", end="")
print("E", sep="")

fruit = "ORANGE"

# Formatting and Aligning Text
print("{:-<30}".format(fruit)) # Left Aligned
print("{:->30}".format(fruit)) # Right Aligned
print("{:-^30}".format(fruit)) # Centered
