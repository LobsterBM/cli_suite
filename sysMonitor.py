from gui import move
import sys
import termgraph
from termgraph import termgraph
import time
import os
#returns percent of cpu usage and list with total memory , available and percentage used
import psutil


def pcLoad():
    return psutil.cpu_percent() , psutil.virtual_memory()[:4]

def printPCusage(LOCK,timer , x, y):

    while True :
        LOCK.acquire()
        move(y, x)
        # sys.stdout.write('\x1b[1A')
        # delete last line
        sys.stdout.write('\x1b[2K')
        sys.stdout.write('\x1b[2K')
        sys.stdout.write('\x1b[2K')
        sys.stdout.write('\x1b[2K')



        print("CPU : " + str(round(psutil.cpu_freq()[0])) + " MHz "  )

        cpu , ram = pcLoad()
        label = ['cpu']
        if(cpu == 0) : cpu = cpu+0.1
        data = [[cpu/cpu, cpu-(cpu/cpu)]]
        bar_fill = [[cpu//2 +1 , (100-cpu)//2]]
        terminal_width = int(os.popen('stty size', 'r').read().split()[1])
        len = 2
        args = {
            'title' : None ,
            'width' : round(terminal_width * 0.7) ,
            'format' : '{:<5.1f}' ,
            'suffix' :  '%',
            'no_labels' : True ,
            'color' : None ,
            'vertical' : False ,
            'stacked' : True ,
            'different_scale' : False ,
            'calendar' : True ,
            'start_dt' : None ,
            'cusom_tick' :'' ,
            'delim' : '| ' ,
            'verbose' : False,
            'version' : False
        }
        colors= [91,94]
        res = termgraph.stacked_graph(label , data , bar_fill , len,args, colors )

        labelRam = ['Ram']
        rampercent = (ram[3]/ram[0])*100
        print("Ram : " + str((ram[3])//1000000) + " MB / " + str(ram[0]//1000000) + " MB" )

        sys.stdout.write('\x1b[2K')

        dataRam = [[rampercent / rampercent, rampercent
                    - (rampercent / rampercent)]]
        bar_fillRam = [[rampercent // 2 + 1, (100 - rampercent) // 2]]
        colorsRam = [92, 95]
        res = termgraph.stacked_graph(labelRam, dataRam, bar_fillRam, len, args, colorsRam)
        LOCK.release()
        time.sleep(timer)
