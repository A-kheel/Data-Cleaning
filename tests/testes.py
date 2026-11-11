#for pangdataload
from modules.pangdataload import load_sensor_data 
def test_load_data():
    sensor_data = load_sensor_data()
    assert len(sensor_data) == 16

    for recording in sensor_data.values():
        assert(len(recording)) == 3

    for acc, gyr, grav in sensor_data.values():
        assert list(acc.columns) == ["time", "seconds_elapsed","acc_z", "acc_y", "acc_x"]
        assert list(gyr.columns) == ["time", "seconds_elapsed", "gyr_z", "gyr_y", "gyr_x"]
        assert list(grav.columns) == ["time", "seconds_elapsed", "grav_z", "grav_y", "grav_x"]

print("good")   


#for pangdatamerge

import pandas as pd
from modules.pangmergeload import merge_sensor_data

def test_merge_sensor_data():

    acc = pd.DataFrame({
        "time": [1000000000, 1020000000, 1040000000],
        "seconds_elapsed": [0, 0.02, 0.04],
        "acc_x": [1, 2, 3],
        "acc_y": [4, 5, 6],
        "acc_z": [7, 8, 9]
    })
    gyr = pd.DataFrame({ 
    "time" : [1000000000, 1020000000, 1040000000],
    "seconds_elapsed" : [0, 0.02, 0.04],
    "gyr_x" : [1, 2, 3],
    "gyr_y" : [4, 5, 6],
    "gyr_z" : [7, 8, 9]
    })
    grav = pd.DataFrame({ 
        "time" : [1000000000, 1020000000, 1040000000],
        "seconds_elapsed" : [0, 0.02, 0.04],
        "grav_x" : [1, 2, 3],
        "grav_y" : [4, 5, 6],
        "grav_z" : [7, 8, 9]
    })

    result = merge_sensor_data(acc, gyr, grav)

    assert isinstance(result, pd.DataFrame)
    assert len(result.columns) == 11
    assert len(result) == 3
    assert result.isna().sum().sum() == 0



#paste this in the terminal, python -m pytest tests/testes.py -v to test