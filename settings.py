import json
import os
import sys
import time

import geopy
import threading

WEATHER_URL1= "https://api.openweathermap.org/data/2.5/onecall?lat="
WEATHER_URL2= "&lon="
WEATHER_URL3= "&exclude=minutely,alerts&units=metric&appid="
WEATHER_API = "54b3dcca7174c677c2ac815e7cb497b9"




#API_URL = 'https://api.coindesk.com/v1/bpi/'
API_URL = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency='



CRYPTO = ["BTC"]
FIAT = "EUR"



LAT = 50.41
LON = 4.44
LOCATION = "Louvain-la-Neuve"
WEATHER_HOURS = 5

MODULES = ["system" , "crypto" , "weather"]

TIMER = 1

"""
-m will add modules separated by ","
-rm will remove modules 
-crypto can add crypto , separated by "," 
-rc will remove cryptos 
edit currency 
-w to update weather region 
TODO : XxY to make a grid in terminal 

  



"""
#update settings if args are null then values don't change
def updateSettings(addCrypto , removeCrypto , defaultCurrency , addModules , removeModules, weatherLocation , weatherHours, timer):

    f = open("settings.json", 'r')
    data = json.load(f)
    f.close()
    global CRYPTO , MODULES , WEATHER_HOURS , LOCATION , FIAT ,TIMER ,LAT,LON



    if addCrypto != None:
        for i in addCrypto:
            if i not in CRYPTO:
                CRYPTO.append(i.upper())
        data['settings'][0]['cryptoCurrency'] = CRYPTO
    if removeCrypto != None:
        for i in removeCrypto:
            if i in CRYPTO:
                CRYPTO.remove(i)
        data['settings'][0]['cryptoCurrency'] = CRYPTO

    if defaultCurrency != None:
        FIAT = defaultCurrency
        data['settings'][0]['fiatCurrency'] = defaultCurrency


    if addModules != None:
        for i in addModules:
            if i not in MODULES:
                MODULES.append(i)
        data['settings'][0]['modules'] = MODULES
    if removeModules != None:
        for i in removeModules:
            if i in MODULES:
                MODULES.remove(i)
        data['settings'][0]['modules'] = MODULES

    if weatherLocation != None :
        LOCATION = weatherLocation
        data['settings'][0]['location'] = LOCATION

        try:

            location = geopy.Nominatim(user_agent="cli").geocode(LOCATION)
            LAT = location.latitude
            LON = location.longitude

        except:
            sys.exit("Error :  location not found !")

        data['settings'][0]['latitude'] = LAT
        data['settings'][0]['longitude'] = LON


    if weatherHours != None :
        WEATHER_HOURS = weatherHours
        data['settings'][0]['weatherHours'] = LOCATION
    if timer != None:
        TIMER = timer
        data['settings'][0]['timer'] = TIMER

    with open('settings.json' , 'w') as f :
        json.dump(data,f)
        f.close()


def setSettings():
    f = open('settings.json','r')
    settings = json.load(f)
    f.close()
    global LOCATION,CRYPTO,FIAT,LAT,LON,WEATHER_HOURS,MODULES,TIMER
    CRYPTO = settings['settings'][0]['cryptoCurrency']
    FIAT = settings['settings'][0]['fiatCurrency']
    LOCATION = settings['settings'][0]['location']
    WEATHER_HOURS =  settings['settings'][0]['weatherHours']

    MODULES = settings['settings'][0]['modules']
    LAT = settings['settings'][0]['latitude']
    LON = settings['settings'][0]['longitude']

    TIMER = settings['settings'][0]['timer']


def startup():
    #if settings file doesn't exist create one

    if os.path.isfile('settings.json') == False:
        defaultSettings={"settings" :[{ 'cryptoCurrency': ['BTC'],'fiatCurrency': 'USD', 'modules' : ["system" , "crypto" , "weather"] , 'weatherHours' : 5 , 'timer' : 1 , 'location' : "Louvain-la-Neuve" , 'latitude' : 50.669 , 'longitude' : 4.613 }]}
        fp = open('settings.json','w')
        json.dump(defaultSettings,fp)
        fp.close()

    setSettings()


