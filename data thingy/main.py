import tkinter as tk
from gui import MatplotlibGUI  # Import MatplotlibGUI from gui.py
from data_visualizer import generate_brightness_graph, generate_violin_plots
from csv_separator import split_csv, clean_and_extract_cell_info, clean_brightness

def main():
    original_file = '/Users/albert2/Desktop/data thingy/031824 Astrocyte Analysis - Nuclei - FOV 8 AD.csv'
    cell_info_path = 'cell_info.csv'
    brightness_path = 'brightness.csv'

    root = tk.Tk()
    

    split_csv(original_file, cell_info_path,brightness_path)
    clean_brightness()
    clean_and_extract_cell_info()

    violin_plots = generate_violin_plots()
    brightness_plots = generate_brightness_graph()

    graphs = []
    graphs.append(brightness_plots[0])
    for plot in violin_plots:
        graphs.append(plot)


    app = MatplotlibGUI(root, graphs)
    root.mainloop()


if __name__ == '__main__':
    main()
