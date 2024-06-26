import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from csv_separator import split_csv, clean_brightness, clean_and_extract_cell_info
#from matplotlib.widgets import RadioButtons
from matplotlib.backend_bases import NavigationToolbar2

original_file = '/Users/albert2/Documents/GitHub/Group11DataVisualizer/data thingy/031824 Astrocyte Analysis - Nuclei - FOV 8 AD.csv 21-40-06-675.csv'
cell_info_path = 'cell_info.csv'
brightness_path = 'brightness.csv'
split_csv(original_file, cell_info_path,brightness_path)
clean_brightness()
clean_and_extract_cell_info()
cell_info_df = pd.read_csv(cell_info_path)
cell_info_df.columns = cell_info_df.columns.str.strip()
brightness_df = pd.read_csv(brightness_path, header=None)

params_to_plot = ['Peak Intensities', 'Distances', 'Peak Value', 'Amplitude', 'FWHM (s)', 
                  'Mean Rise Rate (s^-1)', 'Stdev Mean Rise Rate(s^-1)', 'Peak Rise Rate (s^-1)', 
                  'Mean Fall Rate(s^-1)', 'Stdev Mean Fall Rate(s^-1)', 'Peak Fall Rate (s^-1)']


with open('other.csv', 'r') as file:
    lines = file.readlines()
    cut_frame = int(lines[1].strip().split(': ')[1])
    live_cells_range = list(map(int, lines[2].strip().split(': ')[1].split('-')))
    dead_cells_range = list(map(int, lines[3].strip().split(': ')[1].split('-')))
    control = int(lines[4].strip().split(': ')[1])

live_cells = range(live_cells_range[0]-1, live_cells_range[1])
dead_cells = range(dead_cells_range[0]-1, dead_cells_range[1])

# Extract data for live and dead cells
live_cells_data = brightness_df.iloc[:, live_cells]
dead_cells_data = brightness_df.iloc[:, dead_cells]
print(live_cells_data)

peaks_live = []
for col in live_cells_data.columns:
    peak_value, peak_index = live_cells_data[col].max(), live_cells_data[col].idxmax()
    peaks_live.append((peak_value, peak_index))

peaks_dead = []
for col in dead_cells_data.columns:
    peak_value, peak_index = dead_cells_data[col].max(), dead_cells_data[col].idxmax()
    peaks_dead.append((peak_value, peak_index))



fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
time_points = np.arange(1, brightness_df.shape[0] + 1)

# Plot live cells data on the first subplot
for i, (col, (peak_value, peak_index)) in enumerate(zip(live_cells_data.columns, peaks_live)):
    ax1.plot(brightness_df.index * 3, live_cells_data[col], label=f'Live Cell {live_cells_range[0] + i} (peak: {peak_value:.2f} at t={(peak_index+1)*3})')  # Annotate peak value and time
ax1.set_title('Live Cells')
ax1.set_ylabel('Normalized Brightness')
ax1.legend(loc='upper right')
ax1.grid(True)



# Plot dead cells data on the second subplot
for i, (col, (peak_value, peak_index)) in enumerate(zip(dead_cells_data.columns, peaks_dead)):
    ax2.plot(brightness_df.index * 3, dead_cells_data[col], label=f'Dead Cell {dead_cells_range[0] + i} (peak: {peak_value:.2f} at t={(peak_index+1)*3})')  # Annotate peak value and time
ax2.set_title('Dead Cells')
ax2.set_xlabel('Time (seconds)')
ax2.set_ylabel('Normalized Brightness')
ax2.legend(loc='upper right')
ax2.grid(True)

# Add overall title
plt.suptitle('Brightness Over Time for Live and Dead Cells')

# Display the plot
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.gca().set_xlim(left=0)
plt.gca().set_ylim(bottom=0)
plt.show()







live_cells_data = cell_info_df.iloc[live_cells, :]

'''
def create_violin_plot(param, cell_info_df):

    fig, ax = plt.subplots()  # Create a separate figure for each plot
    sns.violinplot(x=cell_info_df[param], orient='h', density_norm='width', linewidth=2, ax=ax)
    ax.set_ylabel('Density')
    ax.set_xlabel(param)
    ax.set_title(f'Violin Plot of {param}')
    return fig

# Create a list to store the pre-generated figures
violin_plots = []
for param in params_to_plot:
    violin_plots.append(create_violin_plot(param, live_cells_data))
'''

                
def update_plot():
    global fig, axes
    for ax in axes:
        ax.clear()  # Clear the current axes
    
    start_idx = current_page * 6
    end_idx = min(start_idx + 6, len(params_to_plot))
    
    for ax, param in zip(axes, params_to_plot[start_idx:end_idx]):
        sns.violinplot(x=cell_info_df[param], orient='h', density_norm='width', linewidth=2, ax=ax)
        ax.set_ylabel('Density')
        ax.set_xlabel(param)
        ax.set_title('')
    
    fig.suptitle('Violin Plots of Params ('+str(start_idx+1) + ' - ' + str(end_idx)+')', fontsize=16)
    fig.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to make space for the title
    fig.canvas.draw_idle()  # Redraw the figure

# Function to plot subplots
def init_subplots():
    f, a = plt.subplots(2, 3, figsize=(10, 8))
    a = a.flatten()
    return f, a

# Global variable to track the current page
current_page = 0
# Initialize plot
fig, axes = init_subplots()

def on_next():
    global current_page
    max_page = (len(params_to_plot) - 1) // 6
    if current_page < max_page:
        current_page += 1
        update_plot()

def on_prev():
    global current_page
    if current_page > 0:
        current_page -= 1
        update_plot()

# Callback function for button press events
def on_click(event):
    if event.key == 'right':
        on_next()
    elif event.key == 'left':
        on_prev()
# Connect the event handler
fig.canvas.mpl_connect('key_press_event', on_click)

o_back = NavigationToolbar2.back
o_forward = NavigationToolbar2.forward
def n_back(self, *args, **kwargs):
    on_prev()
    o_back(self, *args, **kwargs)
def n_forward(self, *args, **kwargs):
    on_next()
    o_forward(self, *args, **kwargs)
NavigationToolbar2.back = n_back
NavigationToolbar2.forward = n_forward

update_plot()
plt.show()
NavigationToolbar2.back = o_back
NavigationToolbar2.forward = o_forward
#plt.clf()

'''
plt.figure(figsize=(10, 8)) #20, 15))
for i, param in enumerate(params_to_plot):
    plt.subplot(4, 3, i+1)
    sns.violinplot(x=cell_info_df[param], orient='h', density_norm='width', linewidth=2)
    plt.ylabel('Density')
    plt.xlabel(param)
    plt.title(f'Violin Plot of {param}')
plt.tight_layout()
plt.show()
'''

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