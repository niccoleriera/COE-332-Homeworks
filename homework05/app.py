from flask import Flask 
import redis 
import json

app = Flask(__name__)
rd = redis.Redis(host='172.17.0.17', port = '6379')

@app.route('/data', methods = ['POST'])
def load_data() -> str:
    """
    This function reads in Meteorite Landing data and stores it in the Redis database.

    Returns:
    A string that lets the user know that the data has been read from the file.
    """
    data = json.load(open('ML_Data_Sample.json', 'r'))
    rd.set('k1', json.dumps(data))
    return f'Data has been read from file\n'

@app.route('/data', methods = ['GET'])
def read_data():
    """
    This function takes the Meteorite Landing data that has been loaded as a key and returns it as a JSON list.
    Returns:
    The JSON list of the Meteorite Landing data.
    """
    return json.loads(rd.get('k1'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
