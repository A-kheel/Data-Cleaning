from modules.pangdataload import load_sensor_data 
from modules.pangmergeload import merge_sensor_data

sensor_data = load_sensor_data()
acc, gyr, grav = sensor_data["away1"]
print(acc.columns)
print("Accelerometer:", len(acc))
print("Gyroscope:", len(gyr))
print("Gravity:", len(grav))
print("Acc = Gyr:", acc["time"].equals(gyr["time"]))
print("Acc = Grav:", acc["time"].equals(grav["time"]))

#fopr mersge

merged_data = merge_sensor_data(acc, gyr, grav)

print(merged_data.columns)
print(merged_data.shape)
print(merged_data.isna().sum())
print(merged_data[merged_data.isna().any(axis=1)])

