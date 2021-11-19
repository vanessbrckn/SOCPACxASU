import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import MySQLdb as mdb

sqlHost = "bkiazvlmf2da3jw6cpwq-mysql.services.clever-cloud.com"
sqlUser = "u0q348qzs0ebwle4"
sqlPW = "7KemNoGxkh1NcsoTlytG"
sqlDBname = "bkiazvlmf2da3jw6cpwq"

#this connects our program to the database

db = mdb.connect(host=sqlHost, user=sqlUser,
                 password=sqlPW, database=sqlDBname)

def locationQuery(lat,long):
    locquery = "SELECT b.lid FROM "+sqlDBname+".bases b WHERE "+str(lat)+" = b.lat AND "\
    +str(long)+" = b.lon;"

    cursor = db.cursor()
    cursor.execute(locquery)
    locationID = cursor.fetchone()



    return locationID

def planeQuery(locationID):

    planequery = "SELECT * FROM "+sqlDBname+".plane p "\
        "WHERE p.location="+str(locationID)+";"

    cursor = db.cursor()
    cursor.execute(planequery);
    records = cursor.fetchall()
    rows = "plane ID\tModelNumber\n"

    for row in records:
        rows += str(row[0]) + "\t\t\t" + str(row[1]) + "\n"

    return records

def threatLevel(locationID):

    threatquery = "SELECT l.threatlevel FROM "+sqlDBname+".Location l "\
    "WHERE l.lid = "+str(locationID)+";"

    cursor = db.cursor()
    cursor.execute(threatquery)
    threatlevel = cursor.fetchall()

    return threatlevel

def appropriatePlane(planes, threatlevel):

    options = ""

    for plane in planes:
        if plane[4] == threatlevel:
            options = plane

    return options

#this will query the planes that are available, and see which ones have that firepower

#This will query the planes and the crew there and give personnel that have the licenses to
#fly/operate those planes
def crewQueryLicense(planes, locationID):

    crewquery = "SELECT c.name, p.pid FROM "+sqlDBname+".crew c, "+sqlDBname+".plane p"\
        "WHERE c.location = "+locationID+" AND c.licenses = p.licenses AND"\
        "p.location = "+locationID+";"

    cursor = db.cursor()
    cursor.execute(crewquery)
    availablecrew= cursor.fetchall()

    return availablecrew

#this one just returns the crews that are available at that base
def crewQuery(locationID):

    cquery = "SELECT c.pid FROM "+sqlDBname+".crew c WHERE c.location ="+locationID+";"

#This will determine if the plane selected for the mission can house where it's going
#I dont know how to do this yet...
#def airportSizeTest(pane):

#    airportquery = "SELECT a.capacity FROM "+sqlDBname+".airport a, "+sqlDBname+".plane p, "\
#        "WHERE a.capacity >= p.pid "

loc = locationQuery(34.946222,69.264639)
print("Location ID of hardcoded lat and long, we will get from map:")
print(loc[0])
print("plane specs from queried location:")
planes = planeQuery(loc[0])
print(planes)
print("threat Level, which is also the firepower of plane, we may not alway need this spec, honestly:")
tlevel = threatLevel(loc[0])
print(tlevel[0][0])
print("this is the plane's spec that can handle the \"threat level\":")
print(appropriatePlane(planes, tlevel[0][0]))


