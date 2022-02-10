import json
import math

MARS_RADIUS = 3389.5

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( MARS_RADIUS * d_sigma )

def time_to_sample(meteorite_data_list, composition):
    """
    Given a list of meteorite data dictionaries and the string that allows access to composition, this function will add a string of each compositions sample time to a list while also calculating the total time it will take to sample 
    all of the compositions in the list. This total time is added at the end of the list. 

    Args:
        meteorite_data_list: The list of dictionaries of meteorite data.
        composition: The string that contains the meteorite's composition.

    Returns:
        return(sample_time_list): The list of sample times as well as the total sample time.
    """
    sample_time_list = []
    time = 0
    for i in range(len(meteorite_data_list)):
        if  (meteorite_data_list[i][composition] == 'stony'):
            sample_time_list.append('time to sample = 1 hr')
            time += 1
        elif (meteorite_data_list[i][composition] == 'iron'):
            sample_time_list.append('time to sample = 2 hr')
            time += 2
        elif (meteorite_data_list[i][composition] == 'stony-iron'):
            time += 3
            sample_time_list.append('time to sample = 3 hr')
        else:
            pass
    sample_time_list.append(time)
    return(sample_time_list)

def time_to_travel(meteorite_data_list, lat_string, lon_string):
    """
    Given a list of meteorite data dictionaries and the strings that access latitude and longitude, this function calculates the amount of time it will take to get from one site to the other and adds a string to a list that states the 
    amount of time it will take. The total time is added at the end of the list. 

    Args:
        meteorite_data_list: The list of dictionaries of meteorite data.
        lat_string: The key string that contains the latitude.
        lon_string: The key string that contains the longitude.

    Returns:
        return(travel_time_list): The list that contains the travel times as well as the total travel time.
    """
    total_time = 0
    travel_time_list = []
    lat1 = 16.0
    lon1 = 82.0
    for i in range(len(meteorite_data_list)):
        lat2 = meteorite_data_list[i][lat_string]
        lon2 = meteorite_data_list[i][lon_string]
        dist = calc_gcd(lat1, lon1, lat2, lon2)
        time = dist/10
        total_time += time
        lat1 = lat2
        lon1 = lon2
        travel_time_list.append('time to travel = ' + str(time) + ' hr, ')
    travel_time_list.append(total_time)
    return (travel_time_list)

def main():
    with open('sites.json', 'r') as f:
        ms_data = json.load(f)
        site_data = ms_data['sites']
        travel_time = time_to_travel(ms_data['sites'], 'latitude', 'longitude')
        sample_time = time_to_sample(ms_data['sites'], 'composition')
        total_time = travel_time[len(site_data)] + sample_time[len(site_data)]
        for i in range(len(site_data)):
            leg_format = 'leg = ' + str(i+1) + ','
            print(leg_format , travel_time[i], sample_time[i])
        print('number of legs = ' + str(len(site_data)) , ', total time elapsed = ' + str(total_time) )

main()
