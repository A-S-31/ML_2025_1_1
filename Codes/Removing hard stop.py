#Remove all the trackID which are hard stop that is avg_velocity<1
import pandas as pd

df = pd.read_csv('/acceleration.csv')

track_avg = df.groupby('trackID')['average_velocity'].mean().reset_index()

trackIDs_to_remove = track_avg[track_avg['average_velocity'] < 1]['trackID'].tolist()

df_filtered = df[~df['trackID'].isin(trackIDs_to_remove)]

df_filtered.to_csv("/content/removedhardstop.csv", index=False)

from google.colab import drive
drive.mount('/content/drive')

df_filtered.to_csv("/content/drive/My Drive/removedhardstop.csv", index=False)
