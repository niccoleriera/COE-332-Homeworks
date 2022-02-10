import json
import random

def random_descriptions(random_data, loop_number):
    random_data = {}
    random_data['site_id'] = loop_number
    random_data['latitude'] = random.uniform(16.0, 18.0)
    random_data['longitude'] = random.uniform(82.0, 84.0)
    meteorite_composition = ['stony', 'iron', 'stony-iron']
    random_data['composition'] = random.choice(meteorite_composition)
    return(random_data)

def main():
    data = {}

    data['sites'] = []

    for x in range(5):
        data['sites'].append(random_descriptions(data['sites'], x+1))

    with open('sites.json','w') as o:
        json.dump(data, o, indent = 2)

main()
