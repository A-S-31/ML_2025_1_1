#Scatter plot - acceleration vs frameNo
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('/removedhardstop .csv')

# Define moving average function
def moving_average(series, window_size=1000):
    return series.rolling(window=window_size, min_periods=1).mean()

# Create the plot
plt.figure(figsize=(10, 6))

# Group data by trackID and create a scatter plot for acceleration
for track_id, track_data in df.groupby('trackID'):
    smoothed_acceleration = moving_average(track_data['acceleration'], window_size=5)
    plt.scatter(track_data['frameNo'], smoothed_acceleration, label=f'Track {track_id}', alpha=0.5, s=10)

# Labels and title
plt.xlabel("Frame Number")
plt.ylabel("Smoothed Acceleration")
plt.title("Smoothed Acceleration Over Time for Each Track")
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1), markerscale=5)
plt.grid(True)

# Show the plot
plt.show()