import data 
import os

PATH = "../data/sched"

for file in os.listdir(PATH):
    name = file[:-4]
    print(name)
    times = data.get_next_arrival_times("eb_6_street_sw_ctrain_station", 0, 5)
    print(times)
