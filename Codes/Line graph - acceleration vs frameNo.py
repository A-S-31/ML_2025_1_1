#Line graph - acceleration vs frameNo
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/removedhardstop .csv')

def moving_average(series, window_size=1000):
    return series.rolling(window=window_size, min_periods=1).mean()

plt.figure(figsize=(10, 6))

for track_id, track_data in df.groupby('trackID'):
    smoothed_acceleration = moving_average(track_data['acceleration'], window_size=5)
    plt.plot(track_data['frameNo'], smoothed_acceleration, label=f'Track {track_id}', alpha=0.7)

plt.xlabel("Frame Number")
plt.ylabel("Smoothed Acceleration")
plt.title("Smoothed Acceleration Over Time for Each Track")
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
plt.grid(True)

plt.show()