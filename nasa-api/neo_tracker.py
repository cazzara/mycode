import requests
import json
import webbrowser
import time
import sys
from pprint import pprint
from neo import Neo
"""
neo_tracker.py

Author : Chris Azzara
Purpose : Interface with NASA APIs to retrieve information about Near Earth Objects
"""
API_KEY = "L0BfzsAt1hTJVtm3O3j3Ekil8i98zwG33b9nnfpI"
NEO_URL = "https://api.nasa.gov/neo/rest/v1/feed?"
api = "&api_key={}"

def getNEOs(url):
    """
    Query NASA's NEO feed.
    By default the start date is today and end date
    is a week from today.
    """
    print(url)
    neo_list = []
    nasa_resp = requests.get(url)
    neo_data = json.loads(nasa_resp.text)
    if 'error_message' in neo_data.keys():
        print(neo_data['error_message'])
        sys.exit(-2)
    total_neo_count = neo_data['element_count']
    print("\n**********Total Near Earth Objects**********")
    print("Looks like there are {} total NEOs passing close by in the selected time frame".format(total_neo_count))
    neos = neo_data['near_earth_objects']
    # print(len(neos)) # Default: 8, today plus 7 days from now
    neo_keys = list(neos.keys())
    neo_keys.sort()
    for key in neo_keys:
        print("There will be {:2} NEOs whizzing by on {}".format(len(neos[key]), key))
        ns = neos[key]
        for n in ns:
            neo_list.append(\
                Neo(n['name'],\
                    n['neo_reference_id'],\
                    n['close_approach_data'][0],\
                    n['estimated_diameter'],\
                    n['is_potentially_hazardous_asteroid'],\
                    n['nasa_jpl_url'],\
                    n['absolute_magnitude_h'])\
                )
    return neo_list

def displayInfo(l):
    print("\n**********Detailed Info**********")
    print("{:^20} {:^20} {:^20} {:^20} {:^20} {:^20} {:^20} {:^20}".format("Name", "Miles", "Kilometers", "Astronomical Units" , "Lunar Distance", "Miles per Hour", "Kilometers per Hour", "Kilometers per Sec"))

def setStartDate():
    print("Enter the start date to retrieve NEO information: ")
    print("Date must be in YYYY-MM-DD format")
    start = input("Hit enter to just use today's date\n")
    start_date = "start_date={}"
    if not start:
        start = time.strftime("%Y-%m-%d") # YYYY-MM-DD
    return start_date.format(start)
        
def setEndDate():
    print("Enter the end date to retrieve NEO information: ")
    print("Date must be in YYYY-MM-DD format")
    end = input("Hit enter to see all NEOs for next 7 days\n")
    end_date = "&end_date={}"
    return end_date.format(end)

if __name__ == "__main__":
    #NEO_URL += setStartDate()
    #NEO_URL += setEndDate()
    #NEO_URL += api.format(API_KEY)
    NEO_URL = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2018-05-31&end_date=2018-05-31&api_key=L0BfzsAt1hTJVtm3O3j3Ekil8i98zwG33b9nnfpI"
    list_of_neos = getNEOs(NEO_URL)
    displayInfo(list_of_neos)
    
