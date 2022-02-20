import json
import socket

SERVER_ADDRESS,PORT = "127.0.0.1",8080
SERVER_ADDRESS = "127.0.0.1:8080"
class ArrivalData:

	def __init__(self, item_dict):

		self.station = item_dict["station"]
		self.direction = item_dict["direction"]
		self.line = item_dict["line"]
		self.hour = int(item_dict["hour"])
		self.minute = int(item_dict["minute"])
		self.time = 60*self.hour + self.minute

	def __str__(self):

		return f"the {self.line} line train will arrive at {self.station} station at {str(self.hour)}:{str(self.minute)}"



def schedule_from_json(json_string):

	sched_list = json.loads(json_string)
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

	connection = socket.create_connection((SERVER_ADDRESS,PORT))
	request_str = str.encode(station)
	connection.send(request_str)
<<<<<<< HEAD
	reply_size = int(connection.recv(16))
	num_rcved = 0
	while num_rcved < reply_size:
		json_datab = connection.recv(reply_size)
		num_rcved += len(json_datab)
		if not json_datab:
=======
	num_rcved = 0
	while num_rcved < 16:
		size_rcved = connection.recv(16 - num_rcved)
		num_rcved += len(size_rcved)
	reply_size = int(size_rcved)
	num_rcved = 0
	while num_rcved < reply_size:
		json_datab = connection.recv(reply_size - num_rcved)
		num_rcved += len(json_data)
		if not json_data:
>>>>>>> 9899fc7efef4e5db55b01668d6aba4b3d3716649
			break
	json_data = json_datab.decode("ascii")

	connection.close()


	data = schedule_from_json(json_data)

	for item in data:

            if item.time > current_time and len(returnlist) < number_of_arrivals:
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
