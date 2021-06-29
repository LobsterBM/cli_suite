from gui import move
from settings import API_URL , FIAT
import requests
import termcolor
from termcolor import cprint , colored
import time
def createURL(history):
    return API_URL+'currentprice.json'


def requestJsonReader(json):
    return json['bpi'][FIAT]['rate']

#TODO : create 24 hour max and min

def printInterface(LOCK ,url,timer ,y,x ):
    val = '0'
    prevColor = ["yellow", 'on_red']
    while True :
        json = requests.get(url).json()
        currentPrice = requestJsonReader(json)
        currentColor = ["yellow" ,'on_red' ]

        if currentPrice != val :
            prevColor = currentColor
            if (currentPrice > val):
                currentColor = ["grey", "on_green"]
            LOCK.acquire()
            move(y,x)
            """        
            print("+-------------------------------------------------+")
            print("::::::::::::::::::::::::::::")
            print(":+:    :+:   :+:   :+:    :+:")
            print("+:+    +:+   +:+   +:+")
            print("+#++:++#+    +#+   +#+")
            print("+#+    +#+   +#+   +#+")
            print("#+#    #+#   #+#   #+#    #+#")
            print("#########    ###    ########")
            print("+-------------------------------------------------+")
            """

            text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])

            cprint("BTC" , "grey", "on_yellow")
            cprint("+-------------------------------------------------+", "grey", "on_yellow")

            cprint('previous  :   ' + str(val) , prevColor[0] , prevColor[1])
            cprint('current   :   ' + str(currentPrice) , currentColor[0] , currentColor[1])
            cprint("+-------------------------------------------------+", "grey", "on_yellow")
            val = currentPrice
            LOCK.release()
            time.sleep(timer)

