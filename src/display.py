from data import ArrivalData
from datetime import datetime

LENGTH = 50

def display(data):

    print("Station" + (" " * (LENGTH - 7)) + "Line" + (" "*(LENGTH - 4)) + "Time")

    now = datetime.now()

    for i in data:

        timem = 0
        times = 0
        timeh = i.hour - now.hour
        if (i.minute - now.minute < 0):
            timeh -= 1
            timem = now.minute - i.minute
        else:
            timem = i.minute - now.minute

        timestr = str(i.hour - now.hour) + ":"

        if (i.second - now.second):
            timem -= 1
            times = now.second - i.second
        else:
            times = i.second - now.second

        timestr += str(timem) + ";" + str(times)


        timestr += str(i.minute - now.minute) + ";"
        timestr += str(i.second - now.second) + ";"
        print(i.station + (" " * (LENGTH-len(i.station))) + i.line + (" " * (LENGTH-len(i.line))) + timestr)


a = ArrivalData({"station":"Univeristy Station","line":"69th Street","hour":20,"minute":30,"second":20})
b = ArrivalData({"station":"University Station","line":"Tuscany","hour":20,"minute":30,"second":20})

display([a,b])
