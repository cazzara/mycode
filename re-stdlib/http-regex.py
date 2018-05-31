import requests
import re


print("Enter a URL to search: ", end="")
url = input()
if not url.startswith("http://"):
    url = "http://" + url
print()
print("Enter a word to search for: ", end="")
search = input()
print()
print("Awesome! Let's search \"{}\" for \"{}\"".format(url, search))
resp = requests.get(url)
searchText = resp.text

match = re.search(search, searchText)
if match:
    print("Found match :)")
    print(match)
else:
    print("No match :(")
    
