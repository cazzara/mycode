from datetime import datetime # required to use datetime


## WRITE YOUR OWN CODE TO DO SOMETHING. ANYTHING.
# SUGGESTION: Replace with code to print a question to screen and collect data from user.
# MORE DIFFICULT -- Place the response(s) in a list & continue asking the question until the user enters the word 'quit'

startTime = datetime.now()    # returns the time of right now from the datetime object
# Note that datetime is an object, not a simple string.
## Explore the statrTime object
print('The startTime hour is: ' + str(startTime.hour))
print('The startTime minute is: ' + str(startTime.minute))
print('The startTime day is: ' + str(startTime.day))
print('The startTime year is: ' + str(startTime.year))

print("This is how long it takes Python to count to 50:")
for i in range(50):
    pass
## Figure out how long it took to do that something 
print('The code took: ' + str(datetime.now() - startTime) + ' to run.')
