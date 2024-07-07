import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

live_path = '/Users/albert2/Documents/GitHub/Group11DataVisualizer/data thingy/compiled data live - Sheet1.csv'
dead_path = '/Users/albert2/Documents/GitHub/Group11DataVisualizer/data thingy/compiled data dead - Sheet1.csv'
live_df = pd.read_csv(live_path)
dead_df = pd.read_csv(dead_path)

live_cytoplasm_df = live_df.iloc[:601]
live_nuclei_df = live_df.iloc[602:]
dead_cytoplasm_df = dead_df.iloc[:601]
dead_nuclei_df = dead_df.iloc[602:]

live_cytoplasm_peaks = live_cytoplasm_df.max()
live_nuclei_peaks = live_nuclei_df.max()
dead_cytoplasm_peaks = dead_cytoplasm_df.max()
dead_nuclei_peaks = dead_nuclei_df.max()

peaks_df = pd.DataFrame({
    'Live Cytoplasm': live_cytoplasm_peaks,
    'Live Nuclei': live_nuclei_peaks,
    'Dead Cytoplasm': dead_cytoplasm_peaks,
    'Dead Nuclei': dead_nuclei_peaks
})
peaks_df.to_csv('cell_peak_brightness.csv')

live_cytoplasm_avg_peak = live_cytoplasm_peaks.mean()
live_nuclei_avg_peak = live_nuclei_peaks.mean()
dead_cytoplasm_avg_peak = dead_cytoplasm_peaks.mean()
dead_nuclei_avg_peak = dead_nuclei_peaks.mean()

print(f"Average Peak Brightness Values:")
print(f"Live Cells Cytoplasm Average Peak: {live_cytoplasm_avg_peak:.2f}")
print(f"Live Cells Nuclei Average Peak: {live_nuclei_avg_peak:.2f}")
print(f"Dead Cells Cytoplasm Average Peak: {dead_cytoplasm_avg_peak:.2f}")
print(f"Dead Cells Nuclei Average Peak: {dead_nuclei_avg_peak:.2f}")

live_cytoplasm_peak = live_cytoplasm_df.max().max()
live_cytoplasm_peak_col = live_cytoplasm_df.max().idxmax()
live_nuclei_peak = live_nuclei_df.max().max()
live_nuclei_peak_col = live_nuclei_df.max().idxmax()
dead_cytoplasm_peak = dead_cytoplasm_df.max().max()
dead_cytoplasm_peak_col = dead_cytoplasm_df.max().idxmax()
dead_nuclei_peak = dead_nuclei_df.max().max()
dead_nuclei_peak_col = dead_nuclei_df.max().idxmax()

fig, axs = plt.subplots(2, 2, figsize=(14, 10))
axs[0, 0].plot(live_cytoplasm_df.index * 3, live_cytoplasm_df, linestyle='-')
axs[0, 0].set_title('Live Cells Cytoplasm')
axs[0, 0].set_xlabel('Time (seconds)')
axs[0, 0].set_ylabel('Total Brightness')
axs[0, 0].grid(True)
axs[0, 0].annotate(f'Brightest: {live_cytoplasm_peak:.2f}\n{live_cytoplasm_peak_col}\nAvg Peak: {live_cytoplasm_avg_peak:.2f}', 
                   xy=(0.5, 0.9), xycoords='axes fraction', fontsize=12,
                   horizontalalignment='center', verticalalignment='center', 
                   bbox=dict(facecolor='white', alpha=0.5))

axs[0, 1].plot(live_nuclei_df.index * 3 - 1750, live_nuclei_df, linestyle='-')
axs[0, 1].set_title('Live Cells Nuclei')
axs[0, 1].set_xlabel('Time (seconds)')
axs[0, 1].set_ylabel('Total Brightness')
axs[0, 1].grid(True)
axs[0, 1].annotate(f'Brightest: {live_nuclei_peak:.2f}\n{live_nuclei_peak_col}\nAvg Peak: {live_nuclei_avg_peak:.2f}', 
                   xy=(0.5, 0.9), xycoords='axes fraction', fontsize=12,
                   horizontalalignment='center', verticalalignment='center', 
                   bbox=dict(facecolor='white', alpha=0.5))

axs[1, 0].plot(dead_cytoplasm_df.index * 3, dead_cytoplasm_df, linestyle='-')
axs[1, 0].set_title('Dead Cells Cytoplasm')
axs[1, 0].set_xlabel('Time (seconds)')
axs[1, 0].set_ylabel('Total Brightness')
axs[1, 0].grid(True)
axs[1, 0].annotate(f'Brightest: {dead_cytoplasm_peak:.2f}\n{dead_cytoplasm_peak_col}\nAvg Peak: {dead_cytoplasm_avg_peak:.2f}', 
                   xy=(0.5, 0.9), xycoords='axes fraction', fontsize=12,
                   horizontalalignment='center', verticalalignment='center', 
                   bbox=dict(facecolor='white', alpha=0.5))

axs[1, 1].plot(dead_nuclei_df.index * 3 - 1750, dead_nuclei_df, linestyle='-')
axs[1, 1].set_title('Dead Cells Nuclei')
axs[1, 1].set_xlabel('Time (seconds)')
axs[1, 1].set_ylabel('Total Brightness')
axs[1, 1].grid(True)
axs[1, 1].annotate(f'Brightest: {dead_nuclei_peak:.2f}\n{dead_nuclei_peak_col}\nAvg Peak: {dead_nuclei_avg_peak:.2f}', 
                   xy=(0.5, 0.9), xycoords='axes fraction', fontsize=12,
                   horizontalalignment='center', verticalalignment='center', 
                   bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()
plt.show()

print(f"Peak Brightness Values:")
print(f"Live Cells Cytoplasm Peak: {live_cytoplasm_peak:.2f}, Column: {live_cytoplasm_peak_col}")
print(f"Live Cells Nuclei Peak: {live_nuclei_peak:.2f}, Column: {live_nuclei_peak_col}")
print(f"Dead Cells Cytoplasm Peak: {dead_cytoplasm_peak:.2f}, Column: {dead_cytoplasm_peak_col}")
print(f"Dead Cells Nuclei Peak: {dead_nuclei_peak:.2f}, Column: {dead_nuclei_peak_col}")

t_stat_cytoplasm, p_value_cytoplasm = ttest_ind(live_cytoplasm_peaks, dead_cytoplasm_peaks, equal_var=False)
t_stat_nuclei, p_value_nuclei = ttest_ind(live_nuclei_peaks, dead_nuclei_peaks, equal_var=False)

t_stat_live, p_value_live = ttest_ind(live_cytoplasm_peaks, live_nuclei_peaks, equal_var=False)
t_stat_dead, p_value_dead = ttest_ind(dead_cytoplasm_peaks, dead_nuclei_peaks, equal_var=False)

print(f"T-test Results:")
print(f"Cytoplasm: t-statistic = {t_stat_cytoplasm:.2f}, p-value = {p_value_cytoplasm:.5f}")
print(f"Nuclei: t-statistic = {t_stat_nuclei:.2f}, p-value = {p_value_nuclei:.5f}")
print(f"Live: t-statistic = {t_stat_live:.2f}, p-value = {p_value_live:.5f}")
print(f"Dead: t-statistic = {t_stat_dead:.2f}, p-value = {p_value_dead:.5f}")
