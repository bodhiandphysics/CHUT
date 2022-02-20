from data import ArrivalData
from datetime import datetime
import os
import time
import curses


LENGTH = 25

def display(data):

    toReturn = ("Station" + (" " * (LENGTH - 7)) + "Line" + (" "*(LENGTH - 4)) + "Time") + "\n"

    now = datetime.now()

    for i in data:


        timeh = (i.time // 60) - now.hour
        timem = (i.minute % 60) - now.minute
        if (timem < 0):
            timeh -= 1
            timem = 60 + timem

        timestr = str(timeh).zfill(2) + ":" + str(timem).zfill(2)


        toReturn += (i.station + (" " * (LENGTH-len(i.station))) + i.line + (" " * (LENGTH-len(i.line))) + timestr) + "\n"

    return toReturn


a = ArrivalData({"station":"Univeristy Station","line":"69th Street","hour":20,"minute":30})
b = ArrivalData({"station":"University Station","line":"Tuscany","hour":20,"minute":55,"second":20})


def fancy(w):
    while(True):
        w.clear()
        w.addstr(display([a,b]))
        w.refresh()
        time.sleep(5)


curses.wrapper(fancy)


