import json
import os
import time

import geocoder
import threading

WEATHER_URL1= "https://api.openweathermap.org/data/2.5/onecall?lat="
WEATHER_URL2= "&lon="
WEATHER_URL3= "&exclude=minutely,alerts&units=metric&appid="
WEATHER_API = "54b3dcca7174c677c2ac815e7cb497b9"
API_URL = 'https://api.coindesk.com/v1/bpi/'
#API_URL = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur'
DAY = 0
HOUR = 0
MINUTE = 0
CRYPTO = "BTC"
FIAT = "EUR"
LAT = 50.41
LON = 4.44
REGION = "Belgium"
LOCATION = "Louvain-la-Neuve"
WEATHER_HOURS = 5


#update settings if args are null then values don't change
def updateSettings(defaultCrypto , defaultCurrency , duration):

    f = open("settings.json", 'r')
    data = json.load(f)
    f.close()


    if defaultCurrency != None:
        data['settings'][0]['fiatCurrency'] = defaultCurrency
    if defaultCrypto != None:
        data['settings'][0]['cryptoCurrency'] = defaultCrypto
    if duration != None :
        if duration.length == 3 :
            days = duration[0]
            duration = duration [1::]
        else : days = 0
        if duration.length ==2:
            hours = duration[0]
            duration = duration[1::]
        else : hours = 0
        if duration.length == 1:
            minutes = duration[0]
        else : minutes = 0
        data['settings'][0]['days'] = days
        data['settings'][0]['hours'] = hours
        data['settings'][0]['minutes'] = minutes

    with open('settings.json' , 'w') as f :
        json.dump(data,f)
        f.close()

def setSettings():
    f = open('settings.json','r')
    settings = json.load(f)
    f.close()
    CRYPTO = settings['settings'][0]['cryptoCurrency']
    FIAT = settings['settings'][0]['fiatCurrency']
    DAY = settings['settings'][0]['days']
    HOUR = settings['settings'][0]['hours']
    MINUTE = settings['settings'][0]['minutes']
    return CRYPTO,FIAT,DAY,HOUR,MINUTE



def startup():
    #if settings file doesn't exist create one
    g= geocoder.ip('me')
    LAT,LON = g.latlng

    REGION = str(g.current_result)[1:-1]

    if os.path.isfile('settings.json') == False:
        defaultSettings={"settings" :[{ 'cryptoCurrency': 'BTC','fiatCurrency': 'USD', 'days': '0', 'hours': '0','minutes': '30'}]}
        fp = open('settings.json','w')
        json.dump(defaultSettings,fp)
        fp.close()


