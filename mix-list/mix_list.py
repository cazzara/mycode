#!/usr/bin/env python3

# Socket and link state information stored in a list
my_list = ["192.168.0.5", 5060, "UP"]

# Display the contents of the list to the user
print("The first item of the list (IP): {}".format(my_list[0]))
print("The second item of the list (port): {}".format(my_list[1]))
print("The last item of the list (state): {}".format(my_list[2]))

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# Print all of the data on one line
print("When I {} into IP address {} or {} I am unable to ping ports {}, {}, or {}".format(new_list[-1], new_list[3], new_list[4], new_list[0], new_list[1], new_list[2]))

