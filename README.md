# Group11DataVisualizer

4 Python libraries are needed for this code, numpy, pandas, matplotlib, and seaborn.
Before running this code, make sure you have all 4 libraries installed.

If you don't have any installed yet, just run 
pip install -r requirements.txt

## How to Use
  - Download the data from google sheets as a .csv file, for example: 031824 Astrocyte Analysis - Nuclei - FOV 8 AD
  - Drag this csv file into the folder 
  - Go to data_visualizer.py and change the original_file path to the path to the csv you just put in there
  - Do the same for csv_separator.py
  - Hit run in data_visualizer.py
  - After the first plot is generated, take a look at the data that is outputted. If it says 600 rows at the bottom, that is correct.
  - If it says 601, change line 37 in csv_separator.py to         file.writelines(lines[3:])
  - If it says 599, change it to        file.writelines(lines[2:])



## Quick Note
  - Neuron: Index or label.
  - FPS: Data capture rate.
  - Peak Intensities: Maximum observed intensity.
  - Distances: Spatial or peak-to-peak distance.
  - Peak Location (s): Time of peak intensity.
  - Peak Value Amplitude: Height of the peak above baseline.
  - FWHM (s): Duration of the peak.
  - Mean Rise Rate (s^-1): Average rate of intensity increase.
  - Stdev Mean Rise Rate(s^-1): Variability in rise rate.
  - Peak Rise Rate (s^-1): Maximum rate of intensity increase.
  - Mean Fall Rate(s^-1): Average rate of intensity decrease.
  - Stdev Mean Fall Rate(s^-1): Variability in fall rate.
  - Peak Fall Rate (s^-1): Maximum rate of intensity decrease.
