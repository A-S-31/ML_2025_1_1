import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV data
data = pd.read_csv('velocity_data_2.csv')

# Sort data by track ID and frame number
data = data.sort_values(by=['trackID', 'frameNo'])

# Compute velocity change (delta_v)
data['delta_v'] = data.groupby('trackID')['instantenous_velocity'].diff().fillna(0)

# Define stop classification based on velocity change
hard_stop_threshold = -5  # Example: If velocity drops by more than 5 units
momentary_stop_threshold = -1  # Example: If velocity drops by 1-5 units

def classify_stop(v):
    if v <= hard_stop_threshold:
        return 'Hard Stop'
    elif v <= momentary_stop_threshold:
        return 'Momentary Stop'
    else:
        return 'No Stop'

data['stop_type'] = data['delta_v'].apply(classify_stop)

# Choose a track ID to visualize
trackID_to_plot = data['trackID'].unique()[0]  # Change as needed
vehicle_data = data[data['trackID'] == trackID_to_plot]

# Plot velocity change over time with only points
plt.figure(figsize=(12, 6))
plt.scatter(vehicle_data['frameNo'], vehicle_data['instantenous_velocity'], label='Velocity', marker='o', color='blue')
#plt.scatter(vehicle_data['frameNo'][vehicle_data['stop_type'] == 'Hard Stop'], 
            #vehicle_data['instantenous_velocity'][vehicle_data['stop_type'] == 'Hard Stop'], 
            #color='red', label='Hard Stop', marker='x', s=100)
#plt.scatter(vehicle_data['frameNo'][vehicle_data['stop_type'] == 'Momentary Stop'], 
            #vehicle_data['instantenous_velocity'][vehicle_data['stop_type'] == 'Momentary Stop'], 
            #color='orange', label='Momentary Stop', marker='o', s=100)

plt.xlabel('Frame Number')
plt.ylabel('instantenous Velocity')
plt.title(f'Velocity Change for Track ID {trackID_to_plot}')
plt.legend()
plt.show()

# Print summary
print(data[['trackID', 'frameNo', 'instantenous_velocity', 'delta_v', 'stop_type']])