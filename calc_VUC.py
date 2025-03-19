import pandas as pd
import numpy as np
import sys
import os
import math


def calculate_VUC(folder_path):
    # Construct the file paths based on the folder_path passed in sys.argv
    output_file_path = os.path.join(folder_path, "VUC_data_foam.csv")

    df = pd.read_csv(output_file_path)
    df = df[(df['U_2'] > 0)]

    total_area = sum(df['Quality'])
    area_weighted_av_velocity = sum(df['Quality']*df['U_2'])/total_area
    VUC = (math.sqrt(((sum(((df['U_2']-area_weighted_av_velocity)**2)*df['Quality']))/total_area)))/area_weighted_av_velocity

    return [VUC]

if __name__ == "__main__":
    # Ensure the folder path is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python calc_VUC.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    results = calculate_VUC(folder_path)

    # Print the results as a comma-separated string so the main script can capture them
    print(",".join(map(str, results)))

    

