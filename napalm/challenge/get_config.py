#!/usr/bin/env python3
"""

Author : Chris Azzara
Purpose : This script will read from a file containing username/password and a list of 
          Arista EOS switches, it will then download the running configs of the 
          switches and write them to a file

Expected format of text file:

username
password
ip1
ip2
...
ipN

Usage:
./get_config.py path-to-text-file

"""
from napalm import get_network_driver
import sys


if len(sys.argv) != 2:
    print("Usage:\n./get_config.py path-to-text-file")
    sys.exit(-1)

ip_list = None
try:
    ip_list = open(sys.argv[1])
except BaseException as e:
    print("Error: {}".format(e))
    sys.exit(-1)

## Initialize NAPALM EOS driver
driver = get_network_driver('eos')

## First two lines contain username/password
username = ip_list.readline().strip()
password = ip_list.readline().strip()
count = 0
## Remaining lines contain list of IPs
## Open a connection to the device, get the running config, write it to a file
print("-----Downloading Running Configs-----")
for ip in ip_list:
    device = driver(ip.strip(), username, password)
    print("[+] Connecting to {}".format(ip.strip()))
    device.open()
    print("[+] Downloading Config...")
    config = device.get_config()
    run = config['running']
    file_name = ip.strip()+ ".conf"
    f = open(file_name, 'w')
    print("[+] Writing to {}".format(file_name))
    f.write(run)
    f.close()
    device.close()
    count += 1
print("-----Completed Download for {} Devices-----".format(count))








