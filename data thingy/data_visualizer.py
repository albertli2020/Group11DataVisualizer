import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from csv_separator import split_csv, clean_brightness, clean_and_extract_cell_info




original_file = '/Users/albert2/Desktop/data thingy/031824 Astrocyte Analysis - Nuclei - FOV 8 AD.csv'
cell_info_path = 'cell_info.csv'
brightness_path = 'brightness.csv'
cell_info_df = pd.read_csv(cell_info_path)
cell_info_df.columns = cell_info_df.columns.str.strip()
brightness_df = pd.read_csv(brightness_path)


params_to_plot = ['Peak Intensities', 'Distances', 'Peak Value', 'Amplitude', 'FWHM (s)', 
                  'Mean Rise Rate (s^-1)', 'Stdev Mean Rise Rate(s^-1)', 'Peak Rise Rate (s^-1)', 
                  'Mean Fall Rate(s^-1)', 'Stdev Mean Fall Rate(s^-1)', 'Peak Fall Rate (s^-1)']

def generate_violin_plots():
    plots = []
    for i, param in enumerate(params_to_plot):
        ax = plt.subplot(4, 3, i + 1)
        sns.violinplot(x=cell_info_df[param], orient='h', ax=ax)
        ax.set_ylabel(param)
        ax.set_xlabel('Density')
        ax.set_title(f'Violin Plot of {param}')
        plots.append(ax)

    plt.tight_layout()
    return plots

def generate_brightness_graph():
    plots = [] 
    
    plt.figure(figsize=(15, 10))
    time_points = np.arange(1, brightness_df.shape[0] + 1)
    
    for i in range(brightness_df.shape[1]):
        plt.plot(time_points * 3, brightness_df.iloc[:, i], label=f'Neuron {i+1}')
    
    plt.xlabel('Time (Seconds)')
    plt.ylabel('Brightness')
    plt.title('Brightness Over Time for Each Neuron')
    plt.legend()
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.grid(True)
    plt.tight_layout()
    
    axes = plt.gca()
    plots.append(axes) 
    
    return plots


'''
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
