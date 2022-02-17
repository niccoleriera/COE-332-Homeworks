import json
import logging
import math

logging.basicConfig(level=logging.DEBUG)

DECAY = 0.02
TS = 1.0

def calculate_turbidity(calibration_const: float, detector_current: float) -> float:
    """
    Given a calibration constant and a detector current, this function multiplies the two numbers and returns the result which is the turbidity.

    Args:
        calibration_const(float): The calibration constant.
        detector_current(float): The detector current.
    
    Returns:
        T(float): The product of the input arguments (turbidity). 
    """
    T = calibration_const*detector_current
    return (T)

def calculate_min_time(T0: float) -> float:
    """
    Given a current turbidity, this function takes the log of the turbidity threshold for safe water divided by the current turbidity and divides that result by the log of 1 minus the decay, returning the minimum time it takes to return    below a safe threshold.

    Args: 
        T0(float): The current turbidity.

    Returns:
        Time(float): The minimum time it takes to return below safe threshold.
    """
    if (T0 > TS):
        time = (math.log(TS/T0) / math.log(1-DECAY) )
    else:
        time = 0
    return (time) 

def main():
    with open('turbidity_data.json', 'r') as f:
        tb_data = json.load(f)

    recent_tb_data = tb_data['turbidity_data'][-5:]
    total_turbidity = 0.0

    for i in range (5):
        cal_const = recent_tb_data[i]['calibration_constant']
        det_curr = recent_tb_data[i]['detector_current']
        total_turbidity += calculate_turbidity(cal_const, det_curr)
    
    avg_turbidity = total_turbidity / 5 

    print('Average turbidity based on most recent five measurements = ' + str(avg_turbidity) + ' NTU')
    if (avg_turbidity > 1.0):
        logging.warning('Warning: Turbidity is above threshold for safe use')
    else:
        logging.info('Info: Turbidity is below threshold for safe use')

    print('Minimum time required to return below a safe threshold = ' + str(calculate_min_time(avg_turbidity)) + ' hours')

main()
