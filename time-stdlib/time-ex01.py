#!/usr/bin/env python3
import time # This is required to include time module



## Show how we can convert ticks into a useful time tuple
myTime = time.localtime(time.time()) # pass ticks to localtime
print("The local time touple is: " + str(myTime))
print("The local time touple year is: " + str(myTime[0]))
print("The local time touple month is: " + str(myTime[1]))
print("The local time touple day is: " + str(myTime[2]))
print("The local time touple hour is: " + str(myTime[3]))
print("The local time touple minute is: " + str(myTime[4]))
print("The local time touple second is: " + str(myTime[5]))
print("The local time touple week is: " + str(myTime[6]))
print("The local time touple year is: " + str(myTime[7]))
print("The local time touple daylight savings is: " + str(myTime[8]))

def secsToDays(t):
    # 24 hrs in a day
    # 60 mins in a hr
    # 24 * 60 = 1440 mins/day
    # 60 secs/min
    # 60 * 1440 = 86400 secs/day
    # returns num of days elapsed
    return t/86400

# My birthday
bday = time.strptime("5 Jan 1991", "%d %b %Y")
print("My Birthday")
str_bday = time.asctime(bday)
print(str_bday)
chris_epoch = time.mktime(bday)
## Count the number of ticks from the epoch
ticks = time.time()
print("Seconds since 12:00am, January 1, 1970 (Today): {}".format(ticks))
print("Seconds since 12:00am, January 1, 1970 (Birth): {}".format(chris_epoch))
lifespan_secs = ticks - chris_epoch
print("Seconds elapsed since my birth: {}".format(lifespan_secs))
lifespan_days = secsToDays(lifespan_secs)
print("Days elapsed since my birth: {}".format(lifespan_days))

## Display the time 500 secs from now, 500 days
now = time.time()
then = now + 500
future = now + (500 * 86400) # 86400 secs/day * 500 days = 43200000 secs
print("Time now - {}".format(now))
print("Time 500 secs from now - {}".format(then))
print("Time 500 days from now - {}".format(future))
c_now = time.ctime(now)
c_then = time.ctime(then)
c_future = time.ctime(future)
print("Time now - {}".format(c_now))
print("Time 500 secs from now - {}".format(c_then))
print("Time 500 days from now - {}".format(c_future))
