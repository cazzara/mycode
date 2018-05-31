"""

Author : Chris Azzara
Basic Usage of the Python builtin time library

"""

import time
print("Performance Counter Time - {}".format(time.perf_counter()))
print("Process Time - {}".format(time.process_time()))
"""
The epoch is the point where time starts.
On most systems it is Jan 1 1970 00:00:00 UTC
You can view the epoch with "time.gmtime(0)"
The above method returns a struct_time object and we can
convert it to a nice looking string by using time.asctime()

Attributes of a struct_time object are as follows:
Index	Attribute	Values
0	tm_year	        (for example, 1993)
1	tm_mon	        range [1, 12]
2	tm_mday	        range [1, 31]
3	tm_hour	        range [0, 23]
4	tm_min	        range [0, 59]
5	tm_sec	        range [0, 61] # 60 is a leap second, 61 supported for legacy
6	tm_wday	        range [0, 6]  # Monday is 0
7	tm_yday	        range [1, 366]
8	tm_isdst	0, 1 or -1    # -1 indicates DST info is unknown
N/A	tm_zone	        abbreviation of timezone name
N/A	tm_gmtoff	offset east of UTC in seconds
"""
print()
print("The epoch for this system is - {}".format(time.asctime(time.gmtime(0))))

"""
time.time()

Most Unix systems keep track of the time as the number of seconds since the epoch
The time.time() method returns that as a floating point number
"""
print()
print("The seconds since Jan 1 00:00:00 1970 - {}".format(time.time()))


"""
time.ctime([secs])

A lot of times we'll be given the current time or a time value that is represented
as the number of seconds since the epoch (known as a Unix time stamp)
The ctime() method allows us to take that timestamp and make it look nice
ie:  time.ctime(1527781826) --> 'Thu May 31 15:50:26 2018'
The optional argument secs is an int/float and returns a string
If it's omitted, time() is used
"""
print()
print("The current time is - {}".format(time.ctime()))

""" 
Formatting and Parsing Time

Python provides two interesting methods for manipulating time strings and structs

strftime(format[, t]) -- Convert struct to string ('f' for format)
    If no time t is given to strftime(), it uses localtime()
strptime(string[, format]) -- Convert string to struct ('p' for parse)
    If no format string is given to strptime(), it uses "%a %b %d %H:%M:%S %Y"

Both of those methods use the following format directives:

Directive	Meaning	
%a	        Locale's abbreviated weekday name.	 
%A	        Locale's full weekday name.	 
%b	        Locale's abbreviated month name.	 
%B	        Locale's full month name.	 
%c	        Locale's appropriate date and time representation.	 
%d	        Day of the month as a decimal number [01,31].	 
%H	        Hour (24-hour clock) as a decimal number [00,23].	 
%I	        Hour (12-hour clock) as a decimal number [01,12].	 
%j	        Day of the year as a decimal number [001,366].	 
%m	        Month as a decimal number [01,12].	 
%M	        Minute as a decimal number [00,59].	 
%p	        Locale's equivalent of either AM or PM.	(1)
%S	        Second as a decimal number [00,61].	(2)
%U	        Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.	(3)
%w	        Weekday as a decimal number [0(Sunday),6].	 
%W	        Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.	(3)
%x	        Locale's appropriate date representation.	 
%X	        Locale's appropriate time representation.	 
%y	        Year without century as a decimal number [00,99].	 
%Y	        Year with century as a decimal number.	 
%z	        Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59].	 
%Z	        Time zone name (no characters if no time zone exists).	 
%%	        A literal '%' character.


"""
print()
print("Time Structs usually look like this:\n{}".format(time.localtime()))
print()
print("Using strftime() and a few directives, we can make it look neat:\n{}".format(time.strftime("%A %B %d %I:%M %p", time.localtime())))
print()
print("Or we can parse a string into a time struct using strptime()")
print("\"Jan 5 1991\" converted to a struct :\n{}".format(time.strptime("Jan 5 1991", "%b %d %Y")))

"""
Performance and Process Time

The time module has the perf_counter() and process_time() functions

perf_counter() -- returns the value of a clock with the highest resolution to measure a short duration, includes time elapsed during sleep()
process_time() -- Returns the sum of the system and user CPU time of the current process. Does NOT include time elapsed during sleep
"""  
