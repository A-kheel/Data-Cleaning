import pandas as pd


def merge_sensor_data(acc, gyr, grav):

   
    time_diff = acc["time"].diff() / 1_000_000_000
    average_diff = time_diff.mean()
    acc_sample_rate = 1 / average_diff 
    gyr_time_diff = gyr["time"].diff() / 1_000_000_000
    gyr_average_diff = gyr_time_diff.mean()
    gyr_sample_rate = 1 / gyr_average_diff

    grav_time_diff = grav["time"].diff() / 1_000_000_000
    grav_average_diff = grav_time_diff.mean()
    grav_sample_rate = 1 / grav_average_diff

    if abs(acc_sample_rate - 50) > 0.5:
        print("Accelerometer needs resampling")
    else:
        print("Accelerometer is already 50 Hz")

    if abs(gyr_sample_rate - 50) > 0.5:
        print("Gyroscope needs resampling")
    else:
        print("Gyroscope is already 50 Hz")

    if abs(grav_sample_rate - 50) > 0.5:
        print("Gravity needs resampling")
    else:
        print("Gravity is already 50 Hz")


    acc["time"] = pd.to_datetime(acc["time"], unit="ns")
    gyr["time"] = pd.to_datetime(gyr["time"], unit="ns")
    grav["time"] = pd.to_datetime(grav["time"], unit="ns")

    acc = acc.set_index("time")
    gyr = gyr.set_index("time")
    grav = grav.set_index("time")

    start_time = acc.index[0]
    

    if abs(acc_sample_rate - 50) > 0.5:
        acc = acc.resample("20ms", origin=start_time).mean() 

    if abs(gyr_sample_rate - 50) > 0.5:
        gyr = gyr.resample("20ms", origin=start_time).mean()

    if abs(grav_sample_rate - 50) > 0.5:
        grav = grav.resample("20ms", origin=start_time).mean()

    print(acc_sample_rate, gyr_sample_rate, grav_sample_rate)


    gyr = gyr.drop(columns=["seconds_elapsed"])
    grav = grav.drop(columns=["seconds_elapsed"])

    merged = pd.merge(
        acc, gyr,
        left_index=True,
        right_index=True,
        how="inner"
    )

    yallahmerged = pd.merge(merged, grav,left_index=True,right_index=True,how="inner")

    yallahmerged = yallahmerged.dropna(
        subset=[
            "acc_x", "acc_y", "acc_z",
            "gyr_x", "gyr_y", "gyr_z",
            "grav_x", "grav_y", "grav_z"
        ],
        how="all"
    )

    qalasmerged = yallahmerged.reset_index()
    return qalasmerged