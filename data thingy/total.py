import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

live_path = '/Users/Albert/Documents/GitHub/Group11DataVisualizer/data thingy/compiled data live - Sheet1.csv'
dead_path = '/Users/Albert/Documents/GitHub/Group11DataVisualizer/data thingy/compiled data live - Sheet1.csv'
live_df = pd.read_csv(live_path)
dead_df = pd.read_csv(dead_path)

live_cytoplasm_rows = live_df.shape[0] // 2
dead_cytoplasm_rows = dead_df.shape[0] // 2

live_cytoplasm_df = live_df.iloc[:live_cytoplasm_rows]
live_nuclei_df = live_df.iloc[live_cytoplasm_rows:]
dead_cytoplasm_df = dead_df.iloc[:dead_cytoplasm_rows]
dead_nuclei_df = dead_df.iloc[dead_cytoplasm_rows:]



fig, axs = plt.subplots(2, 2, figsize=(14, 10))
axs[0, 0].plot(live_cytoplasm_df.index * 3, live_cytoplasm_df, linestyle='-')
axs[0, 0].set_title('Live Cells Cytoplasm')
axs[0, 0].set_xlabel('Time (seconds)')
axs[0, 0].set_ylabel('Total Brightness')
axs[0, 0].grid(True)

axs[0, 1].plot(live_nuclei_df.index * 3, live_nuclei_df, linestyle='-')
axs[0, 1].set_title('Live Cells Nuclei')
axs[0, 1].set_xlabel('Time (seconds)')
axs[0, 1].set_ylabel('Total Brightness')
axs[0, 1].grid(True)

axs[1, 0].plot(dead_cytoplasm_df.index * 3, dead_cytoplasm_df, linestyle='-')
axs[1, 0].set_title('Dead Cells Cytoplasm')
axs[1, 0].set_xlabel('Time (seconds)')
axs[1, 0].set_ylabel('Total Brightness')
axs[1, 0].grid(True)

axs[1, 1].plot(dead_nuclei_df.index * 3, dead_nuclei_df, linestyle='-')
axs[1, 1].set_title('Dead Cells Nuclei')
axs[1, 1].set_xlabel('Time (seconds)')
axs[1, 1].set_ylabel('Total Brightness')
axs[1, 1].grid(True)

plt.show()