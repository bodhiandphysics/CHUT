from data import ArrivalData
from datetime import datetime
import os
import time
import curses


LENGTH = 10

def display(w,data):

    y,x = w.getmaxyx()
    w.attron(curses.A_BOLD | curses.A_UNDERLINE)
    w.addstr(0,0,"Station")
    w.addstr(0,x//2-(LENGTH//2),"Line")
    w.addstr(0,x-LENGTH,"Time\n")
    w.attroff(curses.A_BOLD | curses.A_UNDERLINE)

    now = datetime.now()

    for i in range(len(data)):


        timeh = (data[i].time // 60) - now.hour
        timem = (data[i].minute % 60) - now.minute
        if (timem < 0):
            timeh -= 1
            timem = 60 + timem

        timestr = str(timeh).zfill(2) + ":" + str(timem).zfill(2)

        w.addstr(i+1,0," "*x,curses.color_pair((i+1)%2))
         
        w.addstr(i+1,0,data[i].station,curses.color_pair((i+1)%2))
        w.addstr(i+1,x//2-(LENGTH//2),data[i].line,curses.color_pair((i+1)%2))
        w.addstr(i+1,x-LENGTH,timestr,curses.color_pair((i+1)%2))


a = ArrivalData({"station":"Univeristy Station","line":"69th Street","hour":20,"minute":30})
b = ArrivalData({"station":"University Station","line":"Tuscany","hour":20,"minute":55,"second":20})


def fancy(w):


    curses.start_color()
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_YELLOW)
    curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_YELLOW)

    curses.curs_set(0)

    while(True):
        w.clear()
        display(w,[a,b])
        w.refresh()
        curses.napms(5000)


curses.wrapper(fancy)


