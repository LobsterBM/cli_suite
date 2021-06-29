import time
from gui import move
import requests
import terminaltables
from settings import LAT , LON , WEATHER_API,WEATHER_URL1,WEATHER_URL2,WEATHER_URL3 ,REGION
from termcolor import cprint, colored
weatherColor = {
    2 : ["white","on_grey"],
    3 : ["cyan" , "on_blue"],
    5 : ["cyan", 'on_blue'],
    6 : ["white", "on_white"],
    7 : ["magenta", "on_cyan"],
    800 : ["blue", "on_cyan"],
    801 : ["cyan", "on_cyan"],
    802 : ["white","on_grey"],
    803 : ["white","on_grey"],
    804 : ["white","on_grey"]
}

class Weather :
    def __init__(self, temp , wind , weather,id,color,bgcolor):
        self.temp = temp
        self.wind = wind
        self.weather = weather
        self.id = id
        self.color = color
        self.bgcolor = bgcolor



def weatherModule(LOCK , timer , x,y, hours):

    if hours > 12:
        hours = 12
    weatherURL =  WEATHER_URL1 + str(LAT) + WEATHER_URL2 + str(LON) + WEATHER_URL3 + WEATHER_API
    while True :

        weatherData = requests.get(weatherURL).json()
        hourList = weatherData['hourly']
        hourlyWeather = []
        for i in hourList :
            id = int(i['weather'][0]['id'])
            if id<800 :
                color = weatherColor[id//100]
            else:
                color = weatherColor[id]
            hourlyWeather.append(Weather(i['temp'] , i['wind_speed'] , i['weather'][0]['main'], id, color[0] , color[1]))

        weatherTable = [["Time","Temp" , "Weather" , "Wind"]]
        currentHour = int(time.strftime("%H"))
        for i in range(hours) :
            listElem=["{:0>2n}:00".format(currentHour), str(hourlyWeather[i].temp)+"°" , colored(str(hourlyWeather[i].weather), hourlyWeather[i].color,attrs=['bold']) , str(hourlyWeather[i].wind)+" km/h"]
            weatherTable.append(listElem)
            currentHour+=1
            currentHour = currentHour%24


        table_instance = terminaltables.SingleTable(weatherTable, "Weather")
        table_instance.justify_columns[3] = 'center'
        LOCK.acquire()
        move(x, y)
        print(table_instance.table)
        print()
        LOCK.release()
        time.sleep(timer)




    return
