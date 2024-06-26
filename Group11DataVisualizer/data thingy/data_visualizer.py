import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from csv_separator import split_csv, clean_brightness, clean_and_extract_cell_info




original_file = '/Users/albert2/Desktop/data thingy/031824 Astrocyte Analysis - Nuclei - FOV 8 AD.csv'
cell_info_path = 'cell_info.csv'
brightness_path = 'brightness.csv'
split_csv(original_file, cell_info_path,brightness_path)
clean_brightness()
clean_and_extract_cell_info()
cell_info_df = pd.read_csv(cell_info_path)
cell_info_df.columns = cell_info_df.columns.str.strip()
brightness_df = pd.read_csv(brightness_path)


plt.figure(figsize=(15, 10))
time_points = np.arange(1, brightness_df.shape[0] + 1)
for i in range(brightness_df.shape[1]):
    plt.plot(time_points * 3, brightness_df.iloc[:, i], label=f'Neuron {i+1}')
plt.xlabel('Time (Seconds)')
plt.ylabel('Brightness')
plt.title('Brightness Over Time for Each Neuron')
plt.legend()

# Adjust the plot layout to ensure (0,0) is at the corner
plt.gca().set_xlim(left=0)
plt.gca().set_ylim(bottom=0)
plt.grid(True)
plt.tight_layout()
plt.show()


params_to_plot = ['Peak Intensities', 'Distances', 'Peak Value', 'Amplitude', 'FWHM (s)', 
                  'Mean Rise Rate (s^-1)', 'Stdev Mean Rise Rate(s^-1)', 'Peak Rise Rate (s^-1)', 
                  'Mean Fall Rate(s^-1)', 'Stdev Mean Fall Rate(s^-1)', 'Peak Fall Rate (s^-1)']

plt.figure(figsize=(20, 15))
for i, param in enumerate(params_to_plot):
    plt.subplot(4, 3, i+1)
    sns.violinplot(x=cell_info_df[param], orient='h', scale='width', linewidth=2)
    plt.ylabel('Density')
    plt.xlabel(param)
    plt.title(f'Violin Plot of {param}')
plt.tight_layout()
plt.show()



# Heatmap of correlations
correlation_matrix = cell_info_df[params_to_plot].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Heatmap of Correlations Between Parameters')
plt.show()





print("Summary statistics for 'other.csv':")
print(cell_info_df.describe())

# Mean brightness over time for each neuron
mean_brightness = brightness_df.mean(axis=0)
print("\nMean brightness for each neuron:")
print(mean_brightness)

# Correlation between mean brightness and parameters in other.csv
correlations = cell_info_df.corrwith(mean_brightness, axis=0)
print("\nCorrelation between mean brightness and other parameters:")
print(correlations)


'''
Neuron: Index or label.
FPS: Data capture rate.
Peak Intensities: Maximum observed intensity.
Distances: Spatial or peak-to-peak distance.
Peak Location (s): Time of peak intensity.
Peak Value Amplitude: Height of the peak above baseline.
FWHM (s): Duration of the peak.
Mean Rise Rate (s^-1): Average rate of intensity increase.
Stdev Mean Rise Rate(s^-1): Variability in rise rate.
Peak Rise Rate (s^-1): Maximum rate of intensity increase.
Mean Fall Rate(s^-1): Average rate of intensity decrease.
Stdev Mean Fall Rate(s^-1): Variability in fall rate.
Peak Fall Rate (s^-1): Maximum rate of intensity decrease.
'''