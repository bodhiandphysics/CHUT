from data import ArrivalData

def display(data):

    print("Station" + (" " * 10) + "Line" + (" "*13) + "Time")

    for i in data:
        print(i.station + (" " * (17-len(i.station))) + i.line + (" " * (17-len(i.line))) + str(i.time))


a = ArrivalData({"station":"bob","line":"greg","hour":20,"minute":30,"second":20})
b = ArrivalData({"station":"bob2","line":"greg","hour":20,"minute":30,"second":20})

display([a,b])
