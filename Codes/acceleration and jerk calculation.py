# To find acceleration and jerk
import pandas as pd
df = pd.read_csv("/Finaldataset_ML.csv")

df.sort_values(by=['trackID', 'frameNo'], inplace=True)

df['acceleration'] = df.groupby('trackID')['instantaneous_velocity'].diff()

df['jerk'] = df.groupby('trackID')['acceleration'].diff()

df.to_csv("/content/acceleration.csv", index=False)

from google.colab import drive
drive.mount('/content/drive')
df.to_csv("/content/drive/My Drive/acceleration.csv", index=False)

