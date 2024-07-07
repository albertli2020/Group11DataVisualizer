import pandas as pd
import csv
import os

cell_info_file = 'cell_info.csv'
brightness_file = 'brightness.csv'
other_file = 'other.csv'
csv_file = '/Users/Albert/Documents/GitHub/Group11DataVisualizer/data thingy/031824 Astrocyte Analysis - Nuclei - FOV 8 AD.csv 21-40-06-675.csv'  

def split_csv(input_file, output_file1, output_file2):
    df = pd.read_csv(csv_file)
    split = df.shape[1]
    with open(input_file, 'r', newline='') as infile, \
         open(output_file1, 'w', newline='') as outfile1, \
         open(output_file2, 'w', newline='') as outfile2:
        
        reader = csv.reader(infile)
        writer1 = csv.writer(outfile1)
        writer2 = csv.writer(outfile2)
        
        # Write first 20 lines to output_file1
        for index, row in enumerate(reader):
            if not any(row):
                continue
            if index < split:
                writer1.writerow(row)
            else:
                writer2.writerow(row)

def clean_brightness():
    # Read all lines from the file
    with open(brightness_file, 'r', newline='') as file:
        lines = file.readlines()

    # Write all lines except the first two back to the file
    with open(brightness_file, 'w', newline='') as file:
        file.writelines(lines[3:])

def clean_and_extract_cell_info():
    with open(cell_info_file, 'r', newline='') as infile, \
         open(other_file, 'w', newline='') as outfile:
         
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for i, row in enumerate(reader):
            if i < 5:
                writer.writerow([row[14]]) 
            else:
                break


    with open(cell_info_file, 'r', newline='') as infile, \
         open(cell_info_file + '.tmp', 'w', newline='') as tempfile:
        
        reader = csv.reader(infile)
        rewriter = csv.writer(tempfile)
        
        for row in reader:
            rewriter.writerow(row[:14])



    os.replace(cell_info_file + '.tmp', cell_info_file)
