#!/usr/bin/python
import pycountry
from geopy.geocoders import Nominatim
geolocator = Nominatim()

f1 = open('/home/alain/Downloads/ghcnd-stations.csv', 'r')
currentPseudoISO2 = ""
countryISO2 = ""
countryISO3 = ""
for line in f1:
    parts = line.split(',')
    stationID = parts[0]
    pseudoISO2 = stationID[0:2]

    if (currentPseudoISO2 != pseudoISO2):
        currentPseudoISO2 = pseudoISO2
        latitude = parts[1]
        longitude = parts[2]
        latlong = str(latitude) + "," + str(longitude)
        location, (latitude, longitude) = geolocator.reverse(latlong, language = 'en')
        if location:
            location = location.split(',')
            try:
                countryISO = pycountry.countries.get(name = location[-1].strip())
                countryISO2 = countryISO.alpha_2
                countryISO3 = countryISO.alpha_3
                print(stationID + "," + pseudoISO2 + "," + countryISO2 + "," + countryISO3)
            except Exception:
                print(stationID + "," + pseudoISO2)
    #else:
        #print(stationID + "," + countryISO2 + "," + countryISO3)
        
        #currentPseudoISO2 = pseudoISO2
        #print "%s" % (location[-1])
    #print(location.address)
    #print(str(stationID) + " " + str(latitude) + " " + str(longitude))
