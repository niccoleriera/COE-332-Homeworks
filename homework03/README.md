Unit Testing and Turbidity

Objective:
This purpose of this project was to design a code that would calculate the current water turbidity by taking the average of the five most recent recordings, determine whether the turbidity was below a safe threshold using logging techniques, and calculate the minimum time required for turbidity to fall below the safe threshold. Additionally, we made a python script to test whether the functions designed worked the way they were intended. This is meant to point out whether there are design errors in the code and make sure that everything is running smoothly and correctly. 

Instructions:
In order to download the turbidity data onto your personal computer, you must first use wget in your terminal and attach the link as shown:

   wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json

Additionally, you will need to install pytest. To do this you should type the following into your terminal:
    
    pip install -U pytest

You can check that you have installed the correct version by typing the following in your terminal:

    pytest --version

It should say "pytest 7.0.0".


analyze_water.py:
This script calculates the current water turbidity by looping over the last 5 data points and finding the average water turbidity for those five points. It also determines whether the turbidity is below or above the safe threshold by using logging techniques. If it is above the safe threshold that means that the current water turbidity is above 1. Finally, this script also finds the minimum time required for turbidity to fall below the safe threshold by using a exponential decay formula and rearranging variables to solve for time. 

test_analyze_water.py:
This script is the unit testing script. This is meant to make sure that the code is working the way it is meant to, but also that it is not working when it is not meant to. 

How to interpret Output:
You will know that you have succesfully executed the code if you get an ouput similar to this:

Average turbidity based on most recent five measurements = 0.9852 NTU
Info: Turbidity is below threshold for safe use
Minimum time required to return below a safe threshold = 0 hours

The second line may also say "Warning: Turbidity is above threshold for safe use" if the average turbidity is found to be above 1. 