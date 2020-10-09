#!/usr/bin/python3

"""

    Programming Task posted on cuLearn but not required during TA meeting

"""

import http.client
import urllib

key = "7481QW0APO2BO2BU"  # Put your API Key here
def main():
    params = urllib.parse.urlencode({'field1': "L1-F-5", 'field2': "a", 'field3': "haoyu.xu@carleton.ca", 'api_key':key }) 
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPSConnection("api.thingspeak.com:443")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except http.client.HTTPException:
        print("Connection failed")


if __name__ == "__main__":
    main()
