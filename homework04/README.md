# Parsing Meteorite Data and How to Use Containers

This directory contains 4 other files: a Dockerfile, a python script called ml_data_analysis.py, a tester script called test_ml_data_analysis.py, and a JSON file called Meteorite_Landings.JSON. 

## ml_data_analysis.py
This python script has three main functions (check_hemisphere, count_classes, compute_average_mass). Check_hemisphere checks in which hemisphere the object (in this case the meteorite) is located, compute_average_mass computes the average mass of all the items combined, and count_classes counts the amount of times each value of a certain key is found in a list of dictionaries.

##Running the Dockerfile

###Pulling and Using Existing Image
To pull an existing image you should input the following into your command line:
> docker pull niccoleriera/hw04:hw04

After this, you can run the container by doing the following:
> docker run --rm -it niccoleriera/hw04:hw04 /bin/bash

After this step, you should be inside the container. You will know you are inside the container if you see  :
[root@fe55ff4c2f0e /] or something that says root. To exit, type exit.

###Build an Image From the Dockerfile
To build an image from the dockerfile input the following into your commandline (make sure that it does not say root):
> docker build -t niccoleriera/hw04:hw04 .

The . indicates that you are referring to the current directory that you are in.

###Running the Containerized Code Against Sample Data in the Container
To run the ml_data_analysis.py script input the following in the container:
> ml_data_analysis.py /data/Meteorite_Landings.json

The output should look as follows:
'''
Summary data following meteorite analysis:

Average mass of 30 meteor(s):
83857.3 grams

Hemisphere summary data:
There were 21 meteors found in the Northern & Eastern quadrant
There were 6 meteors found in the Northern & Western quadrant
There were 0 meteors found in the Southern & Eastern quadrant
There were 3 meteors found in the Southern & Western quadrant

Class summary data:
The L5 class was found 1 times
The H6 class was found 1 times
The EH4 class was found 2 times
The Acapulcoite class was found 1 times
The L6 class was found 6 times
The LL3-6 class was found 1 times
The H5 class was found 3 times
The L class was found 2 times
The Diogenite-pm class was found 1 times
The Stone-uncl class was found 1 times
The H4 class was found 2 times
The H class was found 1 times
The Iron-IVA class was found 1 times
The CR2-an class was found 1 times
The LL5 class was found 2 times
The CI1 class was found 1 times
The L/LL4 class was found 1 times
The Eucrite-mmict class was found 1 times
The CV3 class was found 1 times
'''

To run the tester script input the following in the container:
> pytest /code/test_ml_data_analysis.py

If it ran correctly, it should say something like "6 passed".

###Running the Containerized Code Against User-Provided Data
To run the containerized code against user-provided data you have to first navigate to the directory in which that data is located. After this, enter the following in the command line (not the container):
> docker run --rm -it -v $PWD:/data niccoleriera/hw04:hw04 /bin/bash

This should add everything you had in that directory into the root directory called /data

To run the ml_data_analysis.py script with the data you provided input the following in the container:
> ml_data_analysis.py /data/your_file_goes_here.json

##What Should Your Input Data Look Like?
Your input data should look like an overall dictionary of a list of dictionaries similar to the following:
'''
{States: [{State: Texas, Capital: Austin}, {State: Georgia, Capital: Atlanta}, {State: Texas, Capital: Albany}]}
'''

If you want additional Meteorite Landing data you can input the following in your terminal to get the data:
> wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json

This will make a file called ML_Data_Sample.json that contains this data. From there you can follow the steps listed under Running the Dockerfile -> Running the Containerized Code Against User-Provided Data to run the containerized scripts against this data.