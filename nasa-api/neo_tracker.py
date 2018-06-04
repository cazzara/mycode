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
    By default the start date is today and end date is a week from today.
    Returns a list of NEO Objects
    """
    # print(url)
    
    nasa_resp = requests.get(url)
    neo_data = json.loads(nasa_resp.text)
    print("Got response")
##    f = open("neos.txt", 'w') # Output returned JSON to a file for offline manipulation
##    print(neo_data, file=f)
##    f.close()
##    sys.exit()
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
    neo_list = [] # Create empty list to store NEO Objects
    for key in neo_keys: # The keys for this dictionary are the 'YYYY-MM-DD' dates specified in the query
        print("There will be {:2} NEOs whizzing by on {}".format(len(neos[key]), key))
        ns = neos[key]
        for n in ns:
            neo_list.append(    # Instantiate a NEO Object and append to the list     
                Neo(n['name'],\
                    n['neo_reference_id'],\
                    n['close_approach_data'][0],\
                    n['estimated_diameter'],\
                    n['is_potentially_hazardous_asteroid'],\
                    n['nasa_jpl_url'],\
                    n['absolute_magnitude_h'])\
                )
    return neo_list

def displayInfo(l, metric):
    if metric:
        print("\n\t\t\t\t\t\t=========Detailed Info=========\n")
        print("\t\t\t\t\t******Miss Distance****** *******Relative Velocity****** ******Estimated Size******")   # Display Metric Headers
        print("{:-^20}{:-^10}{:-^20}{:-^20}{:-^25}{:-^25}{:-^25}".format("Name", "Date", \
                                                                        "Kilometers", "Astronomical Units" , \
                                                                        "Kilometers per Hour", "Max Diameter (Meters)", \
                                                                        "Max Diameter (Kilometers)"))
        for neo in l:
            neo.displayLineMetric()
            
        close_rock, large_rock, fast_rock = getCloserLargerFaster(l, metric)
        print("\n\n\n\t\t\t\t\t\tClosest Rock Incoming:\n")
        print("{:-^20}{:-^10}{:-^20}{:-^20}{:-^25}{:-^25}{:-^25}".format("Name", "Date", \
                                                                        "Kilometers", "Astronomical Units" , \
                                                                        "Kilometers per Hour", "Max Diameter (Meters)", \
                                                                        "Max Diameter (Kilometers)"))
        close_rock.displayLineMetric()
        print("\n\n\n\t\t\t\t\t\tLargest Rock Incoming:\n")
        large_rock.displayLineMetric()
        print("\n\n\n\t\t\t\t\t\tFastest Rock Incoming:\n")
        fast_rock.displayLineMetric()
    else:
        print("\n\t\t\t\t\t\t=========Detailed Info=========\n")
        print("\t\t\t\t\t******Miss Distance****** *******Relative Velocity****** ******Estimated Size******")   # Display Imperial Headers
        print("{:^20}{:^10}{:^20}{:^20}{:^20}{:^25}{:^25}".format("Name", "Date", "Miles",\
                                                                        "Astronomical Units" , "Miles per Hour", \
                                                                        "Max Diameter (Feet)", "Max Diameter (Miles)"))
        for neo in l:
            neo.displayLineImperial()
            
        close_rock, large_rock, fast_rock = getCloserLargerFaster(l, metric)
        print("\n\n\n\t\t\t\t\t\tClosest Rock Incoming:\n")
        print("{:^20}{:^10}{:^20}{:^20}{:^25}{:^25}{:^25}".format("Name", "Date", "Miles",\
                                                                        "Astronomical Units" , "Miles per Hour", \
                                                                        "Max Diameter (Feet)", "Max Diameter (Miles)"))
        close_rock.displayLineImperial()
        print("\n\n\n\t\t\t\t\t\tLargest Rock Incoming:\n")
        large_rock.displayLineImperial()
        print("\n\n\n\t\t\t\t\t\tFastest Rock Incoming:\n")
        fast_rock.displayLineImperial()
        
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

def getCloserLargerFaster(l, metric):
    i = 0
    closestNEO = l[i]
    largestNEO = l[i]
    fastestNEO = l[i]
    for i in range(1, len(l)):
        n = l[i]
        if metric:
            if float(n.approach_data['miss_distance']['kilometers']) < float(closestNEO.approach_data['miss_distance']['kilometers']):
                closestNEO = n
            if float(n.estimated_size['kilometers']['estimated_diameter_max']) > float(largestNEO.estimated_size['kilometers']['estimated_diameter_max']):
                largestNEO = n
            if float(n.approach_data['relative_velocity']['kilometers_per_hour']) > float(fastestNEO.approach_data['relative_velocity']['kilometers_per_hour']):
                fastestNEO = n
        else:
            if float(n.approach_data['miss_distance']['miles']) < float(closestNEO.approach_data['miss_distance']['miles']):
                closestNEO = n
            if float(n.estimated_size['miles']['estimated_diameter_max']) > float(largestNEO.estimated_size['miles']['estimated_diameter_max']):
                largestNEO = n
            if float(n.approach_data['relative_velocity']['miles_per_hour']) > float(fastestNEO.approach_data['relative_velocity']['miles_per_hour']):
                fastestNEO = n
            
    return closestNEO, largestNEO, fastestNEO



def promptForUnits():
    metric = input("Would you like to display the results in \n(1) Metric \nor \n(2) Imperial\n")
    if metric == "1":
        return True
    else:
        return False
    
if __name__ == "__main__":
    NEO_URL += setStartDate()
    NEO_URL += setEndDate()
    NEO_URL += api.format(API_KEY)
    # NEO_URL = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2018-05-31&end_date=2018-05-31&api_key=L0BfzsAt1hTJVtm3O3j3Ekil8i98zwG33b9nnfpI"
    list_of_neos = getNEOs(NEO_URL)
    metric = promptForUnits()
    displayInfo(list_of_neos, metric)
    
    
    
