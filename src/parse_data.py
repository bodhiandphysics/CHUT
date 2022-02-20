from pathlib import Path
import gtfs_kit as gk
import json
import datetime
import sys
import os


def get_todays_sched():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../data/CT_GTFS.zip')
    feed = gk.read_feed(filename, dist_units='km')
    feed.describe()
    feed.validate()

    # read out all stop names / keep ctrain stops
    stops_df = gk.stops.get_stops(feed)
    stops = []
    for index, row in stops_df.iterrows():
        name = row["stop_name"]
        code = row["stop_code"]
        if "CTrain" in name:
            stop = (name, code)
            stops.append(stop)
    # print(stops)

    # get all todays ctrain schedules
    year = datetime.datetime.now().year
    month = '{0:02d}'.format(datetime.datetime.now().month)
    day = '{0:02d}'.format(datetime.datetime.now().day)
    dates = [str(year) + month + str(day)]
    for stop in stops: 
        times_list = []
        if "University" in stop[0]:
            print(stop[0])
            df = gk.build_stop_timetable(feed, stop[1], dates)
        
            for index, row in df.iterrows():
                departure = {}
                time = row["departure_time"].split(":")
                departure["year"] = year
                departure["month"] = month
                departure["day"] = day
                departure["hour"] = time[0]
                departure["minute"] = time[1]
                departure["direction"] = stop[0].split(" ")[0]
                departure["line"] = "red"
                departure["station"] = stop[0]

                times_list.append(departure)

            filename = stop[0].replace(" ", "_").replace("/", "").lower()
            text_file = open("../data/sched/"+ filename + ".json", "w")
            text_file.write(json.dumps(times_list))
            text_file.close()


if __name__ == "__main__":
  get_todays_sched()