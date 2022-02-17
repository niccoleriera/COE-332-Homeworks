from analyze_water import calculate_turbidity, calculate_min_time
import math
import pytest

def test_calculate_turbidity():
    assert calculate_turbidity( 2, 5.1) == 10.2
    assert calculate_turbidity(2.35, 5.21) == (2.35*5.21)
    assert isinstance(calculate_turbidity(3.2, 1), float) == True

def test_calculate_turbidity_exceptions():
    with pytest.raises(TypeError):
        calculate_turbidity('2.4', '3.1')
    with pytest.raises(NameError):
        calculate_turbidity(constant)

def test_calculate_min_time():
    assert calculate_min_time(1.1) == (math.log(1/1.1)/math.log(0.98))
    assert calculate_min_time(0.7) == 0
    assert isinstance(calculate_min_time(1.1), float) == True

def test_calculate_min_time_exceptions():
    with pytest.raises(TypeError):
        calculate_min_time('0.4')
    with pytest.raises(NameError):
        calculate_min_time(turbidity_data)
