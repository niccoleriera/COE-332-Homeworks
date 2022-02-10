


													Putting JSON Into Use


OBJECTIVE:
	This project is meant to write a python script, turn it into a JSON file, and write another python script that accesses the contents of the JSON file and does some calculations with it. The folder contains the python script that writes the JSON file, the JSON file itself, and the python script that accesses the file. The JSON file is meant to have characterisitics of 5 meteorite sites, with this information we are tasked to calculate the time it takes to travel from one site to the other site, which leg of the trip we are on, and how long it will take to sample that particular meteorite.

GENERATE_SITES.PY
	One of the files in this directory is the generate_sites.py. This is the python script that I turned into a JSON file. It makes a dictionary of lists that are also dictionaries. The one key in the main dictionary is called "sites". In the value of sites, there are five items in a list: site_id, latitude, longitude, and composition. The site_id is supposed to say which site it is (1, 2, 3...), the latitude and longitude is chosen at random--with latitude between 16.0 and 18.0 and longitude between 82.0 and 84.0--, and the composition is also chosen at random between stony, iron, and stony-iron.

CALCULATE_TRIP.PY
	This file is the python script that reads from the JSON file "sites" I created using generate_sites.py, and it calculates the time it takes to travel from one site to the next etc. in the order that it is read in. It also calculates how long it takes to take a sample for each type of composition, and which leg of the trip it is on. Finally, it calculates the number of legs the trip had as well as the total time elapsed. 


To use these files as intended, generate_sites.py must be executed first so that calculate_trip.py can read the file and print its information. Once generate_sites.py is executed, there should be a sites.JSON file located in the directory. If it is executed correctly, calculate_trip.py should print 5 lines with the leg number, time to travel, and time for sample. The last line should state the total time elapsed and total number of legs.  