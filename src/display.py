from data import ArrivalData
from datetime import datetime
import os
import time

LENGTH = 50

def display(data):

    os.system('cmd /c "clear"')

    print("Station" + (" " * (LENGTH - 7)) + "Line" + (" "*(LENGTH - 4)) + "Time")

    now = datetime.now()

    for i in data:


        timeh = (i.time // 60) - now.hour
        timem = (i.minute % 60) - now.minute
        if (timem < 0):
            timeh -= 1
            timem = 60 + timem

        timestr = str(timeh).zfill(2) + ":" + str(timem).zfill(2)


        print(i.station + (" " * (LENGTH-len(i.station))) + i.line + (" " * (LENGTH-len(i.line))) + timestr,flush=True)


a = ArrivalData({"station":"Univeristy Station","line":"69th Street","hour":20,"minute":30})
b = ArrivalData({"station":"University Station","line":"Tuscany","hour":20,"minute":55,"second":20})


while (True):
    display([a,b])
    
    time.sleep(30)
