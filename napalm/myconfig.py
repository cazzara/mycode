#!/usr/bin/env python3

# import code from NAPALM
from napalm import get_network_driver
import json
import pprint as pp
    
# Tell NAPALM to speak "eos" commands to our switches (very cisco-like)
driver = get_network_driver('eos')
    
# Hard-code the switch credentials
device = driver('172.16.2.10', 'admin', 'alta3') 
    
#Equates to: ssh into the switch, login, and enable
device.open() 
    
# Print STARTUP, RUNNING, and CANDIDATE configs 
config = device.get_config()
print("unformatted json:")
print(config)
print("formatted json:")
print(json.dumps(config, indent=4,separators=(',', ': ')))
print("pretty print")
pp.pprint(config)
