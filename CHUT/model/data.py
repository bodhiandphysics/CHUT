import json


class ArrivalData:

	def __init__(self, item_dict):

		self.station = item_dict["station"]
		self.line = item_dict["line"]
		self.hour = int(item_dict["hour"])
		self.minute = int(item_dict["minute"])
		self.second = int(item_dict["second"])
		self.time = 3600*self.hour + 60*self.minute + self.second

	def __str__(self):

		return f"the {self.line} line train will arrive at {self.station} station at {str(self.hour)}:{str(self.minute)}"



def schedule_from_json(json_file):

	sched_list = json.loads(json_file)

	returndat = []

	try: 

		for item_dict in sched_list:

			returndat.append(ArrivalData(item_dict))

		return returndat
	
	except (Exception) as error:
		
		print(error)

def get_next_arrival_times(data, line, current_time, number_of_arrivals):

	returnlist = []

	for item in data:

		if item.line == line and item.time > current_time and len(returnlist) < number_of_arrivals:

			returnlist.append(item)

	return returnlist


def test():

	json_data = """ [{"station": "university", "line": "red", "hour": "11", "minute": "32", "second": "12"},
					 {"station": "university", "line": "red", "hour": "12", "minute": "32", "second": "12"}]"""
	schedule = schedule_from_json(json_data)

	for item in schedule:
		print(item)

	times_list = get_next_arrival_times(schedule, 3600*12, 2)

	for item in times_list:
		print(item)











