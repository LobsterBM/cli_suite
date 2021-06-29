import os.path
import argparse
import time
import psutil
import requests
from termgraph import termgraph
import threading
import sys
import termcolor
from termcolor import colored,cprint
import json

import settings
import weather
import sysMonitor
import cryptoTicker


LOCK = threading.Lock()




if __name__ == '__main__':
    settings.startup()

    parser = argparse.ArgumentParser()
    parser.add_argument('-fiat', '-f',
                        help='update default fiat currency')
    parser.add_argument('-crypto', '-c',
                        help='update default crypto currency')
    parser.add_argument('-time', '-t',nargs='+', type = float,
                        help='update default time : dd hh mm')
    parser.add_argument('-history', nargs='?',
                        help='use time for historical prices')
    parser.add_argument('-timer','-ut', nargs='?',type = int,
                        help='price update timer in seconds')

    args = parser.parse_args()

    if args.time != None and len(args.time) > 3:
        print("-time takes maximum 3 aruments ")
        exit()

    if args.fiat != None or args.crypto != None or args.fiat != None:
        settings.updateSettings(args.crypto, args.fiat, args.time)

    CRYPTO,FIAT,DAY,HOUR,MINUTE = settings.setSettings()

    url = cryptoTicker.createURL(args.history)

    response = requests.get(url)
    pricedata = response.json()

    timer = 5
    if args.timer != None :
        timer = args.timer
    val = 0
    os.system('clear')


    cryptoThread = threading.Thread( target= cryptoTicker.printInterface , args = (LOCK, url , timer ,0,0))
    cryptoThread.start()

    time.sleep(0.1)

    load = threading.Thread(target=sysMonitor.printPCusage, args=(LOCK , timer,0,10,))
    load.start()

    time.sleep(0.1)

    load = threading.Thread(target=weather.weatherModule, args=(LOCK , timer,20,20,settings.WEATHER_HOURS))
    load.start()

    #TODO : instead of main loop , make each function a thread with a loop inside it
    """
     N = 12
    for i in range(N):
         time.sleep(0.5)
         print(f"{i / N * 100:.1f} %", end="\r")
     """





