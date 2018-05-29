#!/usr/bin/env python3

import requests
import json

nasa_iss_endpoint = 'http://api.open-notify.org/astros.json'

resp = requests.get(nasa_iss_endpoint)
resp_json = json.loads(resp.text)

crew_members = resp_json['people']
num_crew = resp_json['number']

print("There are {} people in space".format(num_crew))
print("Their names are: ")
for crew in crew_members:
    print("{:<25}{:<5}".format(crew['name'], crew['craft']))

