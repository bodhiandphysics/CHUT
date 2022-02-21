from data import ArrivalData
from data import get_next_arrival_times
from datetime import datetime
import os
import time
import curses
import signal
import sys

PATH = "../data/sched"
LENGTH = 10


class BetterClass:


    def __init__(self,station,line,times):
        self.station = station
        self.line = line
        self.times = times
        

    def add_time(self,time):
        self.times.append(time)




def display(w,data):

    w.clear()
    curses.curs_set(0)
    now = datetime.now()

    y,x = w.getmaxyx()
    w.attron(curses.A_BOLD | curses.A_UNDERLINE)
    w.addstr(0,0,"Station")
    w.addstr(0,x//2-(LENGTH//2),"Line")
    w.addstr(0,x-LENGTH,"Time(" +str((59-now.second)//10*10 + 10) + ")")
    w.attroff(curses.A_BOLD | curses.A_UNDERLINE)

    for i,obj in enumerate(data):
        if i+2 > y:
            break
        
        w.addstr(i+1,0," "*(x-1),curses.color_pair((i+1)%2))

        w.addstr(i+1,0,obj.station.replace("CTrain Station"," "),curses.color_pair((i+1)%2))
        w.addstr(i+1,x//2-(LENGTH//2),obj.line,curses.color_pair((i+1)%2))

        for j,time in enumerate(obj.times):
            timeh = (time // 60) - now.hour
            timem = time%60 - now.minute
            if (timem < 0):
                timeh -= 1
                timem = 60 + timem

            timestr = f"{str(timeh).zfill(2)}:{str(timem).zfill(2)}"
            w.addstr(i+1,x-((len(obj.times)-j)*8),timestr,curses.color_pair((i+1)%2))

    a = int(now.second/60 *(x-12))
    #w.attron(curses.color_pair(2))
    w.addstr(y-4,a,"\\____")
    w.addstr(y-3,a,"|DD|____T_")
    w.addstr(y-2,a,"|_ |_____|<")
    w.addstr(y-1,a,"@-@-@-oo\\")
    #w.attroff(curses.color_pair(2))
    w.refresh()

def signal_handler(sig, frame):
    curses.endwin()
    sys.exit(0)

def launch():
    w = curses.initscr()
    curses.noecho()
    curses.cbreak()
    w.keypad(True)
    curses.start_color()
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_YELLOW)
    curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_YELLOW)

    return w

def get_data(names,depth):
    while(True):
        try:
            return [obj for name in names for obj in get_next_arrival_times(name,datetime.now(),depth)]
        except:
            continue

def chunk_data(data):
    toReturn = []

    for dat in data:
        if (len(toReturn)==0):
            toReturn.append(BetterClass(dat.station,dat.line,[dat.time]))
        else:
            found = False
            for o in toReturn:
                if dat.station == o.station:
                    o.add_time(dat.time)
                    found = True
            if (not found):
                toReturn.append(BetterClass(dat.station,dat.line,[dat.time]))

    return toReturn

    

def main():
    names = [
        'nb_university_ctrain_station',
        'sb_university_ctrain_station',
        'nb_brentwood_ctrain_station',
        'sb_brentwood_ctrain_station'
    ]


    print("oi")

    data = chunk_data(get_data(names,5))

    print("nice")


    signal.signal(signal.SIGINT, signal_handler)
    w = launch()



    i = 0
    while True:
        if i%1000 == 0:
            data = []
            data = chunk_data(get_data(names,5))

        display(w,data)

        curses.napms(50)
        
        if w.getch == 3:
            raise KeyboardInterrupt

        i += 1
       

if __name__ == '__main__':
    main()
