import pandas as pd


df = pd.read_csv('/content/acceleration.csv')
df = df.sort_values(by=['trackID', 'frameNo'])

increasing_y_tracks = []

for track_id, group in df.groupby('trackID'):
    x_coords = group['x'].values
    y_coords = group['y'].values
    if all(y_coords[i] <= y_coords[i+1] for i in range(len(y_coords) - 1)) and all(x <= 500 for x in x_coords):
        increasing_y_tracks.append(group)

result_df = pd.concat(increasing_y_tracks)
output_path = '/content/upper.csv'
result_df.to_csv(output_path, index=False)

print("First 5 values of increasing y tracks with x ≤ 200:")
print(result_df.head())

files.download(output_path)
