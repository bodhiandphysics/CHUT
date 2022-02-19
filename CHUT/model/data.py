import json


class ArrivalData:

	def __init__(self, item_dict):

		self.station = item_dict["station"]
		self.line = item_dict["line"]
		self.hour = item_dict["hour"]
		self.minute = item_dict["minute"]
		self.second = item_dict["second"]

	def __str__(self):

		return (f"the {self.line} line train will arrive at {self.station} station at {self.hour}:{self.minute}")



def schedule_from_json(json_file):

	sched_list = json.loads(json_file)

	returndat = []

	try: 

		for item_dict in sched_list:

			returndat.append(ArrivalData(item_dict))

		return returndat
	
	except (Exception) as error:
		
		print(error)


def test():

	json_data = """ [{"station": "university", "line": "red", "hour": "11", "minute": "32", "second": "12"},
					 {"station": "university", "line": "red", "hour": "12", "minute": "32", "second": "12"}]"""
	schedule = schedule_from_json(json_data)

	for item in schedule:
		print(item)











