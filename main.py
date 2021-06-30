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
    parser.add_argument('-crypto', '-c', nargs='*',
                        help='updates crypto currency list  ')
    parser.add_argument('-rcrypto', '-rc', nargs='*',
                        help='remvoes crypto currencies from list  ')
    parser.add_argument('-timer', '-t', type = float,
                        help='update timer in seconds')
    parser.add_argument('-location','-l', nargs='?',
                        help='update weather location')
    parser.add_argument('-modules','-m', nargs='*',
                        help='adds modules to interface')
    parser.add_argument('-rmodules', '-rm', nargs='*',
                        help='removes modules from interface ')
    parser.add_argument('-weatherhours', '-w', nargs='?', type = int,
                        help='number of hours for weather prediction ')

    args = parser.parse_args()



    settings.updateSettings(args.crypto , args.rcrypto , args.fiat , args.modules , args.rmodules , args.location , args.weatherhours , args.timer)




    val = 0
    os.system('clear')
    x = 0

    for i in settings.MODULES:
        if i == "weather":
            #TODO make customisable update system instead of 600 for 10 minutes
            weatherThread = threading.Thread(target=weather.weatherModule,
                                    args=(LOCK, 600, x, 20, settings.WEATHER_HOURS))
            weatherThread.start()
            x+=12
            time.sleep(0.2)
        if i == "system":
            load = threading.Thread(target=sysMonitor.printPCusage, args=(LOCK, settings.TIMER, 0, x,))
            load.start()
            x+=8

            time.sleep(0.2)

        if i == "crypto" :
            cryptoThread = threading.Thread(target=cryptoTicker.printInterface,
                                            args=(LOCK, settings.CRYPTO, settings.TIMER, x, 0))
            cryptoThread.start()
            x+=10

            time.sleep(0.2)





