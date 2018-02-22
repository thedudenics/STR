import os
#import glob
#import re
import MySQLdb
import time
from datetime import datetime
from dateutil import parser

conn = MySQLdb.connect(host = "localhost",
                       user = "root",
                       passwd="",
                       db="mobilitydata")
cursor = conn.cursor()

long = ""
lat = ""
alt = ""
time = ""
mincount = 0
hrs = 0
mins = 0
mth = ""
day = ""
year = ""
date = ""
wday = ""

linecount=0

print("- Segregator Initializing")

cursor.execute("TRUNCATE TABLE 000mon")
cursor.execute("TRUNCATE TABLE 001tue")
cursor.execute("TRUNCATE TABLE 002wed")
cursor.execute("TRUNCATE TABLE 003thu")
cursor.execute("TRUNCATE TABLE 004fri")

print("- Tables Truncated")

file = open("data.txt","r")
for line in file:
    data=line.split(" ")
    if linecount%2==0:
        long = data[0]
        lat = data[1]
        temp1 = data[2]
        alt = temp1[:-2]
    else:
        time = data[0]
        h, m = time.split(':')
        mincount = (int(h)*60 + int(m))-450
        hrs = h
        mins = m
        mth = data[1]
        temp2 = data[2]
        day = temp2[:-6]
        year = temp2[-5:-1]
        date = parser.parse(year+"-"+mth+"-"+day)
        wday = date.weekday()
        if (wday==0):
            cursor.execute("INSERT INTO 000mon (Longitude,Latitude,Altitude,MinuteCount,Hours,Minutes,Month,Day,Year,Weekday) VALUES("+long+","+lat+","+alt+","+str(mincount)+","+str(hrs)+","+str(mins)+","+mth+","+day+","+year+","+str(wday)+")")
        elif (wday==1):
            cursor.execute("INSERT INTO 001tue (Longitude,Latitude,Altitude,MinuteCount,Hours,Minutes,Month,Day,Year,Weekday) VALUES("+long+","+lat+","+alt+","+str(mincount)+","+str(hrs)+","+str(mins)+","+mth+","+day+","+year+","+str(wday)+")")
        elif (wday==2):
            cursor.execute("INSERT INTO 002wed (Longitude,Latitude,Altitude,MinuteCount,Hours,Minutes,Month,Day,Year,Weekday) VALUES("+long+","+lat+","+alt+","+str(mincount)+","+str(hrs)+","+str(mins)+","+mth+","+day+","+year+","+str(wday)+")")
        elif (wday==3):
            cursor.execute("INSERT INTO 003thu (Longitude,Latitude,Altitude,MinuteCount,Hours,Minutes,Month,Day,Year,Weekday) VALUES("+long+","+lat+","+alt+","+str(mincount)+","+str(hrs)+","+str(mins)+","+mth+","+day+","+year+","+str(wday)+")")
        elif (wday==4):
            cursor.execute("INSERT INTO 004fri (Longitude,Latitude,Altitude,MinuteCount,Hours,Minutes,Month,Day,Year,Weekday) VALUES("+long+","+lat+","+alt+","+str(mincount)+","+str(hrs)+","+str(mins)+","+mth+","+day+","+year+","+str(wday)+")")
        conn.commit()
    linecount+=1
    print("...")

conn.close()
print("- Segregation Finished")
