import zipfile



def unzip_gtfs():
    with zipfile.ZipFile("../data/CT_GTFS.zip", 'r') as zip_ref:
        zip_ref.extractall("../data/gtfs")

unzip_gtfs()