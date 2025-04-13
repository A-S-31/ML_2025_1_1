import pandas as pd


df = pd.read_csv('/content/removedhardstop123.csv')
df = df.sort_values(by=['trackID', 'frameNo'])

decreasing_tracks = []

for track_id, group in df.groupby('trackID'):
    x_coords = group['x'].values
    y_coords = group['y'].values

    if all(x_coords[i] >= x_coords[i+1] for i in range(len(x_coords) - 1)) and all(y > 1000 for y in y_coords):
        decreasing_tracks.append(group)

result_df = pd.concat(decreasing_tracks)
output_path = '/content/decreasing_x_tracks.csv'
result_df.to_csv(output_path, index=False)

print("First 5 values of decreasing x tracks with y > 1000:")
print(result_df.head())

files.download(output_path)
