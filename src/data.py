import json
import socket

SERVER_ADDRESS = 0
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

	sched_list = json.load(json_file)
	returndat = []

	try: 

		for item_dict in sched_list:

			returndat.append(ArrivalData(item_dict))

		return returndat
	
	except (Exception) as error:
		
		print(error)

#use this function to get the next arrival times.... you'll have to have the data somewhere
def get_next_arrival_times(station, current_time, number_of_arrivals):

	returnlist = []

	connection= socket.create_connection(SERVER_ADDRESS)
	request_str = str.encode(station)
	connection.send(request_str)
	reply_size = int(repr(connection.recv(1024)))
	json_data = repr(connection.recv(reply_size))
	connection.close()


	data = schedule_from_json(json_data)

	for item in data:

		if item.time > current_time and len(returnlist) < number_of_arrivals

			returnlist.append(item)

	return returnlist


def get_next_train_times(station, train)


def test():

	json_data = """ [{"station": "university", "line": "red", "hour": "11", "minute": "32", "second": "12"},
					 {"station": "university", "line": "red", "hour": "12", "minute": "32", "second": "12"}]"""
	schedule = schedule_from_json(json_data)

	for item in schedule:
		print(item)

	times_list = get_next_arrival_times(schedule, 3600*12, 2)

	for item in times_list:
		print(item)
