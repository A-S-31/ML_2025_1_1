#Scatter plot - Instantaneous velocity vs frameNo
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/removedhardstop.csv')

def moving_average(series, window_size=1000):
    return series.rolling(window=window_size, min_periods=1).mean()

plt.figure(figsize=(10, 6))

for track_id, track_data in df.groupby('trackID'):
    smoothed_velocity = moving_average(track_data['instantaneous_velocity'], window_size=5)
    plt.scatter(track_data['frameNo'], smoothed_velocity, label=f'Track {track_id}', alpha=0.5, s=10)

plt.xlabel("Frame Number")
plt.ylabel("Smoothed Instantaneous Velocity")
plt.title("Smoothed Instantaneous Velocity Over Time for Each Track")
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1), markerscale=5)  # Legend outside the plot
plt.grid(True)

plt.show()