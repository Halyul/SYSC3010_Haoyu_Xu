#!/usr/bin/python3

"""

    cpu.py from https://iotdesignpro.com/projects/how-to-send-data-to-thingspeak-cloud-using-raspberry-pi

    Changes:
        - Adapte to run under Python 3
        - Add KeyboardInterrupt to terminate the program
        - Use https
        - Fix typo
        - Update url query name

"""

import http.client
import urllib
import time
from time import sleep

exit = False
key = "CSH3X7KMLDTP2E8Z"  # Put your API Key here
def thermometer():
    #Calculate CPU temperature of Raspberry Pi in Degrees C
    temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
    params = urllib.parse.urlencode({'field1': temp, 'api_key':key }) 
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPSConnection("api.thingspeak.com:443")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(temp)
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except http.client.HTTPException:
        print("Connection failed")
        global exit
        exit = True


if __name__ == "__main__":
    
    while exit is False:
        try : 
            thermometer()
            sleep(1)
        except KeyboardInterrupt:
            print("\nInterrupted, quit.")
            exit = True