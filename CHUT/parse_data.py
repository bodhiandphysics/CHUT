import zipfile



# def unzip_gtfs():
#     with zipfile.ZipFile("../data/CT_GTFS.zip", 'r') as zip_ref:
#         zip_ref.extractall("../data/gtfs")

# unzip_gtfs()

import datetime as dt
from collections import OrderedDict
import sys, os
import dateutil.relativedelta as rd
import json
from pathlib import Path
from typing import List

import utm
import pandas as pd
import numpy as np
import geopandas as gpd
import shapely.geometry as sg
import shapely.ops as so

DIR = Path('..')
sys.path.append(str(DIR))

import gtfs_kit as gk

DATA_DIR = DIR/'data/'

path = DATA_DIR/'CT_GTFS.zip'
feed = gk.read_feed(path, dist_units='km')
feed.describe()
feed.validate()
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
# print(feed.trips.to_string())
dates = ["20220219"]
print(gk.build_stop_timetable(feed, "6816", dates))