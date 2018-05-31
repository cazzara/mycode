import requests
import re
import os
import subprocess


def getExternalIP():
    url = 'http://checkip.dyndns.org'
    resp = requests.get(url)
    ip_info = resp.text
    pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    match = pattern.findall(ip_info)
    print("External IP Address: {}".format(match))

def getInternalIP():
    cmd = subprocess.run(["ifconfig"], stdout=subprocess.PIPE)
    output = cmd.stdout.decode("UTF-8")
    ips = []
    pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    match = pattern.findall(output)
    for ip in match:
        # Exclude 0.0.0.0, subnet masks, and loopback address
        if ip.startswith("0") or ip.startswith("255") or ip.startswith("127"):
            pass
        else:
            ips.append(ip)
    print("Your internal IP addresses are:")
    print(ips)

getExternalIP()
getInternalIP()
