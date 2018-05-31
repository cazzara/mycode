import requests
import json
import webbrowser
from pprint import pprint

"""
apod.py

Author : Chris Azzara
Purpose : Interface with NASA APIs to retrieve information about the Astronomy Picture
        of the Day and open the image in a browser
"""
API_KEY = "L0BfzsAt1hTJVtm3O3j3Ekil8i98zwG33b9nnfpI"

APOD_URL = "https://api.nasa.gov/planetary/apod?api_key={}"


def getAPOD(url, date="", hd=True):
    nasa_resp = requests.get(url)
    apod = json.loads(nasa_resp.text)
    # pprint(apod)
    print("Date: {}".format(apod['date']))
    print("Title: {}".format(apod['title']))
    print("Explanation: {}".format(apod['explanation']))
    pic_url = ''
    if hd:
        pic_url = apod['hdurl']
    else:
        pic_url = apod['url']
    webbrowser.open(pic_url)
    


if __name__ == "__main__":
    getAPOD(APOD_URL.format(API_KEY))
