# Deploying a Software System to Kubernetes using Flask

This project builds upon the previous homework, where we ran a redis container and wrote a flask app to load and retrieve meteorite landing data. In this project, we kept that same flask app and used it to deploy the flask app and redis server in Kubernetes. To do this, we needed to make 5 YML files: a persistent volume claim for the redis data, a deployment for the redis database, a service for the redis database, a deployment for the flask API, and a service for the flask API. All 5 YML files are located in this directory. Additionally, there is a Dockerfile from the previous homework.

## app.py

This flask application has one route /data that can perform both a POST and GET request. The POST request loads the Meteorite Landings data into the Redis database. the GET request reads the data out of Redis and returns it as a JSON list. This is exactly what the application did in the previous homework, none of that has changed. The only thing that is different about this app.py is the host. At the beginning of the application, we originally set "host" in rd = redis.Redis(host='...') to a local host. For this project, we set it to the IP Address given by the redis service in Kubernetes. 

## How to Deploy the Software System

First, you need to ssh into both isp and k8s:
> ssh < username >@isp02.tacc.utexas.edu

> ssh coe332-k8s.tacc.cloud

Once you're in, make sure to copy the yml files that are in this directory into five separate files on Kubernetes. After you have done this, you need to execute the following command for each file:

> kubectl apply -f < file >

To check that your deployments are all running correctly you can do the following:
> kubectl get deployments

There should be two deployments that say "nriera-test-redis" and "nrieratestflask". Everything should be ready.

To check that your pods are all running correctly:
> kubectl get pods

There should be 3 pods that are all running. Two should start with "nrieratestflask" while the other should say "nriera-test-redis".

To check that your services are all running correctly:
> kubectl get services

There should be 2 services: "nriera-test-flask-service" and "nriera-test-redis-service". The port for the flask service should be 5000 whereas the port for the redis service should be 6379.



