 
import pandas as pd
import numpy as np

df = pd.read_csv('Time_bins_ML_results_20251022175629_mut_excl.csv')

rows = []
for video_id, group in df.groupby('Video'):
    values = group.sort_values('Time_bin')['Value'].to_numpy()
    N = len(values)

    # Handle very short videos: put everything in bin 9 to avoid zeros, or distribute as you like
    if N == 0:
        # no data
        for b in range(1, 10):
            rows.append([video_id, b, 0.0])
        continue

    # Build strictly increasing boundaries on nearest indices
    boundaries = [0]
    prev = 0
    for k in range(1, 9):  # 8 internal cuts
        target = int(round(k * N / 9))
        cut = max(prev + 1, min(target, N - (9 - k)))  # keep room for remaining bins
        boundaries.append(cut)
        prev = cut
    boundaries.append(N)  # end exactly at N

    # Slice by boundaries
    for i in range(1, len(boundaries)):
        start, end = boundaries[i-1], boundaries[i]
        rows.append([video_id, i, values[start:end].sum()])

result_df = pd.DataFrame(rows, columns=['Video', 'Bin', 'Sum_Value'])
result_df.to_csv('binned_values_output_equalized.csv', index=False)
