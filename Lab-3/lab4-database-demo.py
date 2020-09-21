#!/usr/bin/env python3
import sqlite3, json
#some initial data
id = 4;
temperature = 0.0;
date = '2020-09-20';
#connect to database file
dbconnect = sqlite3.connect("my.db");
# If we want to access columns by name we need to set row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
# create table called temperature
cursor.execute(""" CREATE TABLE IF NOT EXISTS temperature (
                        id integer,
                        temp numeric,
                         date text
                    ); """)
for i in range(10):
    #execute insert statement
    id += 1;
    temperature += 1.1;
    cursor.execute('''insert into temperature values (?, ?, ?)''',
    (id, temperature, date));
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM temperature');
#print data
for row in cursor:
    print(row['id'],row['temp'],row['date'] );

cursor.execute(""" CREATE TABLE IF NOT EXISTS lab3 (
                        sensorID integer,
                        type text,
                        zone text
                    ); """)
lab3_data = [
    {
        "sensorID": 1,
        "type": "door",
        "zone": "kitchen"
    },{
        "sensorID": 2,
        "type": "temperature",
        "zone": "kitchen"
    },{
        "sensorID": 3,
        "type": "door",
        "zone": "garage"
    },{
        "sensorID": 4,
        "type": "motion",
        "zone": "garage"
    },{
        "sensorID": 5,
        "type": "temperature",
        "zone": "garage"
    }
]

for item in lab3_data:
    cursor.execute('''insert into lab3 values (?, ?, ?)''',
    (item["sensorID"], item["type"], item["zone"]))

dbconnect.commit();

cursor.execute('SELECT * FROM lab3 WHERE zone="kitchen"');

for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] );

cursor.execute('SELECT * FROM lab3 WHERE type="door"');

for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] );

#close the connection
dbconnect.close();