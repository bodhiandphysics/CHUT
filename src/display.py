from data import ArrivalData
from data import get_next_arrival_times
from datetime import datetime
import os
import time
import curses

PATH = "../data/sched"
LENGTH = 10

def display(w,data):

    y,x = w.getmaxyx()
    w.attron(curses.A_BOLD | curses.A_UNDERLINE)
    w.addstr(0,0,"Station")
    w.addstr(0,x//2-(LENGTH//2),"Line")
    w.addstr(0,x-LENGTH,"Time\n")
    w.attroff(curses.A_BOLD | curses.A_UNDERLINE)

    now = datetime.now()

    for i,obj in enumerate(data):
        if i+2 > y:
            break

        timeh = (obj.time // 60) - now.hour
        timem = (obj.minute % 60) - now.minute
        if (timem < 0):
            timeh -= 1
            timem = 60 + timem

        timestr = f"{str(timeh).zfill(2)}:{str(timem).zfill(2)}"

        w.addstr(i+1,0," "*x,curses.color_pair((i+1)%2))
         
        w.addstr(i+1,0,obj.station,curses.color_pair((i+1)%2))
        w.addstr(i+1,x//2-(LENGTH//2),obj.line,curses.color_pair((i+1)%2))
        w.addstr(i+1,x-LENGTH,timestr,curses.color_pair((i+1)%2))

def launch(data):
    w = curses.initscr()
    curses.noecho()
    curses.cbreak()
    w.keypad(True)
    curses.start_color()
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_YELLOW)
    curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_YELLOW)

    curses.curs_set(0)

    while(True):
        w.clear()
        display(w,data)
        w.refresh()
        curses.napms(60000)

    curses.endwin()

def main():
    names = [
        'nb_university_ctrain_station',
        'sb_university_ctrain_station'
    ]
    '''
    names = [
        file[:-5]
        for file in os.listdir(PATH)
    ]
    '''
    data = [
        obj
        for name in names
        for obj in get_next_arrival_times(name,0,5)
    ]
    launch(data)

if __name__ == '__main__':
    main()
