#!/usr/bin/python3

import requests
import json

key = "0XQ73BKEKA9WEKRJ"
result = ""
def main():
    resp = requests.get("https://api.thingspeak.com/channels/1150963/feeds.json?results={}&api_key={}".format(result, key))
    json = resp.json()

    for item, value in json["channel"].items():
        print("Channel {}: {}".format(item, value))
    
    for feed in json["feeds"]:
        print("{} id {} at {}: {}".format(json["channel"]["field1"], feed["entry_id"], feed["created_at"], feed["field1"]))

if __name__ == "__main__":
    main()