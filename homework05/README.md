# Reading and Loading Data from Redis Through Flask

This project runs a redis container and writes a flask app to load data into and retrieve data from it. Specifically, we are loading meteorite landing data. This folder contains two other files: a python script call app.py and a Dockerfile. 

To get the meteorite landing data, you must first input the following into your command line:
> wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json

## How to Run the Redis Container

To run this redis container, first you have to make sure that you have pulled the redis image for version 6:
> docker pull redis:6

Afterwards, input the following to start the redis container:
> docker run -d -p 6422:6379 -v $(pwd)/data:/data:rw --name=nriera-redis redis:6 --save 1 1

What this does is it runs the container in the background, connecting the port I was assigned (6422) to the default port inside of the container (6379). Additionally, it mounts a folder /data inside the container for redis to write all of its state to. The --save 1 1 tells the server to save to 1 backup file every 1 second. 

## Running the Docker Container
To pull the existing containerized app from Docker hub:
> docker pull niccoleriera/flask-ml-data:hw05

To build the container from scratch:
> docker build -t niccoleriera/flask-ml-data:hw05 .

You can put your DockerHub username where I have put mine (niccoleriera) to build and run it.

To run the container:
> docker run -d -p 5022:5000 niccoleriera/flask-ml-data:hw05

## How to Use the Application
This application has one route /data that can perform both a POST and GET request. The POST request loads the Meteorite Landings data into the Redis database. The GET request reads the data out of Redis and returns it as a JSON list. 

To perform the POST request:
> curl -X POST localhost:5022/data

To perform the GET request:
> curl localhost:5022/data

## Meteorite Landing data
This data includes a dictionary of a list of meteorite landings. Each landing contains the following keys: name, id, recclass, mass, reclat, reclong, and geolocation.  
