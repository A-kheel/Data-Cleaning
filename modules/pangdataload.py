import pandas as pd
from pathlib import Path


def load_sensor_data():
    
    data_folder = Path("datas")
    recordings={}
    acc_rename = {"x": "acc_x", "y": "acc_y", "z": "acc_z"}
    gyr_rename = {"x": "gyr_x", "y": "gyr_y", "z": "gyr_z"}
    grav_rename = {"x": "grav_x", "y": "grav_y", "z": "grav_z"}


    for folder in data_folder.iterdir():
        if folder.is_dir():
            acc = pd.read_csv(folder / "Accelerometer.csv")
            gyr = pd.read_csv(folder / "Gyroscope.csv")
            grav = pd.read_csv(folder / "Gravity.csv")

            acc = acc.rename(columns=acc_rename)
            gyr = gyr.rename(columns=gyr_rename)
            grav = grav.rename(columns=grav_rename)
            recordings[folder.name] = (acc, gyr, grav)
    return recordings
