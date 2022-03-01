from ml_data_analysis import compute_average_mass,count_classes,check_hemisphere
import pytest

def test_count_classes():
    assert count_classes([{'a': 2, 'b': 3, 'c':4}, {'a': 2, 'b':6}, {'a':3}], 'a') == {2: 2, 3:1}
    assert count_classes([{'speed': 'fast', 'color':'red'}, {'speed': 'fast', 'color': 'blue'}, {'speed':'slow', 'color':'green'}], 'speed') == {'fast':2, 'slow':1}
    assert count_classes([{1:'fish', 2: 'eagle'}, {1:'zebra', 2:'eagle'}], 1) == {'fish':1, 'zebra':1}
    assert isinstance(count_classes([{'a': 2, 'b': 3, 'c':4}, {'a': 2, 'b':6}, {'a':3}], 'a'), dict) == True

def test_count_classes_exceptions():
    with pytest.raises(TypeError):
        count_classes('a', [{'a': 2, 'b': 3, 'c':4}, {'a': 2, 'b':6}, {'a':3}])

def test_compute_average_mass():
    assert compute_average_mass([{'a' : 1}], 'a') == 1
    assert compute_average_mass([{'a': 1}, {'a': 2}], 'a') == 1.5
    assert compute_average_mass([{'a': 1}, {'a': 2}, {'a': 3}], 'a') == 2

    assert compute_average_mass([{'a':1}, {'a':2}, {'a':3}], 'a') != 3

def test_compute_average_mass_exceptions():
    with pytest.raises(ZeroDivisionError):
        compute_average_mass([], 'a')
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'b': 1}], 'a')
    with pytest.raises(ValueError):
        compute_average_mass([{'a': 1}, {'a': 'x'}], 'a') 
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'a': 2}], 'b')

def test_check_hemisphere():
    assert isinstance(check_hemisphere(90.,90.), str) == True
    assert check_hemisphere(1,-1) == 'Northern & Western'
    assert check_hemisphere(-1,1) == 'Southern & Eastern'
    assert check_hemisphere(-1,-1) == 'Southern & Western'

def test_check_hemisphere_exceptions():
    with pytest.raises(TypeError):
        check_hemisphere('blah', 10.)
    with pytest.raises(ValueError):
        check_hemisphere(1.23, 0.0)
