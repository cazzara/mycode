#!/usr/bin/env python3

import random

## Create a random number generator object 
# This can be used to instantiate multiple instances of PRNGs that are independent of one another and don't share state
r = random.Random()

## Seed random number generator
# This initializes the state of the PRNG, by default it uses the current system time
# Calling this function isn't entirely necessary because the seed function is called when the Random object is created
r.seed()
print("[+] Initialized a PRNG using default seed (system time)")
## Optionally you can specify the source of randomness (os.urandom) or pass in a str, int or bytes like object
# r.seed('banana')

## randrange(start, stop) -- Select a random element from range(start, stop)
print("[+] Print 5 random numbers between 1 and 10 using r.randrange(1, 11)")
for i in range(5):
    print("{} ".format(r.randrange(1, 11)), end='') # Prints a number between 1 and 10
print()

## randint(a, b) -- return a random int N such that a <= N <= b, basically like saying randrange(a, b+1) 
print("[+] Print 5 random numbers between 1 and 10 using r.randint(1, 10)")
for i in range(5):
    print("{} ".format(r.randint(1, 10)), end='')
print()

flavors = ['apple', 'kiwi', 'orange', 'grape', 'strawberry']
print("[+] List of items (flavors):")
print(flavors)
## choice(seq) -- Returns a random element from a non-empty sequence
print("[+] Select a random element from a list using r.choice(flavors)")
print(r.choice(flavors)) # Prints a random flavor from the list

## shuffle(list) -- shuffles a list in place
print("[+] Use r.shuffle(flavors) to randomly redistribute items in a list")
r.shuffle(flavors)
print(flavors)

## sample(population, k) -- returns a list of k elements from a population, sampling without replacement
print("[+] Select k elements from a range or collection (w/o replacement) using r.sample(l, 10)")
l = range(1, 101)
print(r.sample(l, 10)) # print 10 random numbers from 1 - 100

## random() -- returns a random float in the range [0.0, 1.0)
print("[+] Print 5 random floats using r.random()")
for i in range(5):
    print(r.random())
