from urllib.request import * 
from urllib.parse import * 
import json
import sqlite3

def get_data():
    # The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa

    # As of October 2015, you need an API key.
    # I have registered under my Carleton email.
    apiKey = "a808bbf30202728efca23e099a4eecc7"

    # Query the user for a city
    city = input("Enter the name of a city whose weather you want: ")

    # Build the URL parameters
    params = {"q":city, "units":"imperial", "APPID":apiKey }
    arguments = urlencode(params)

    # Get the weather information
    address = "http://api.openweathermap.org/data/2.5/weather"
    url = address + "?" + arguments

    print (url)
    webData = urlopen(url)
    results = webData.read().decode('utf-8')
    # results is a JSON string
    webData.close()

    print (results)
    #Convert the json result to a dictionary
    # See http://openweathermap.org/current#current_JSON for the API

    data = json.loads(results)

    # Print the results

    current = data["main"]
    degreeSym = chr(176)

    # print ("Temperature: %d%sF" % (current["temp"], degreeSym ))
    # print ("Humidity: %d%%" % current["humidity"])
    # print ("Pressure: %d" % current["pressure"] )
    # print ("Wind : %d" % data["wind"]["speed"])

    print()

    return {
        "raw_data": results, # string
        "city": data["name"],
        "timestamp": data["dt"],
        "temp": current["temp"],
        "humidity": current["humidity"],
        "pressure": current["pressure"],
        "wind": data["wind"]["speed"]
    }

def db_operation(data):
    dbconnect = sqlite3.connect("my.db");
    dbconnect.row_factory = sqlite3.Row;
    cursor = dbconnect.cursor();
    cursor.execute(""" CREATE TABLE IF NOT EXISTS {} (
                            timestamp numeric,
                            temp numeric,
                            humidity numeric,
                            pressure numeric,
                            wind numeric,
                            raw text
                        ); """.format(data["city"]))
    cursor.execute('''insert into {} values (?, ?, ?, ?, ?, ?)'''.format(data["city"]), 
    (data["timestamp"], data["temp"], data["humidity"], data["pressure"], data["wind"], data["raw_data"]))
    dbconnect.commit();

    cursor.execute('SELECT * FROM {}'.format(data["city"]));
    for row in cursor:
        print ("Timestamp: %s" % (row["timestamp"]))
        print ("Temperature: %d%sF" % (row["temp"], chr(176)))
        print ("Humidity: %d%%" % row["humidity"])
        print ("Pressure: %d" % row["pressure"] )
        print ("Wind : %d" % row["wind"])
        # print ("Raw data : %s" % row["raw"])
        print()

    #close the connection
    dbconnect.close();

if __name__ == "__main__":
    data = get_data()
    db_operation(data)
    
    
