#!/usr/bin/env python3

# Author : Chris Azzara
# Purpose : This script will parse a Keystone log file to look for login success/failures. Keystone is the log file for the Horizon web GUI to OpenStack

import collections


log_file = open('keystone.common.wsgi')

failedLogins = collections.defaultdict(int)
successfulLogins = 0

for line in log_file:
    if "- - - - -] Authorization failed" in line:
     # Extract the originating IP address of the failed login attempt
        ip = line.split(' ')[-1].strip()
        failedLogins[ip] += 1
    elif "-] Authorization failed" in line:
        successfulLogins += 1
log_file.close()

print("[+] Successful Logins: {}".format(successfulLogins))
print("[-] Failed Logins:")
for ip in failedLogins:
    print("\t{} failed attempts from {}".format(failedLogins[ip], ip))

"""
Sample Output:

[+] Successful Logins: 1
[-] Failed Logins:
	3 failed attempts from 172.16.1.5
"""
