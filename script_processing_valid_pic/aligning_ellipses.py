######### COMPUTE TRANSFORMS TO STANDARDIZE COORDINATE SYSTEM

#### Reference dot = top right corner between electrode and cell
#### Reference length = down straight cell lenght 7.5 mm

# Manually measured in Paint

# Z1 1042 pixel; 2240, 1161
# Z2 1042 pixel;  2240, 1161
# Z3 1063 pixel;  2279, 1191
# Z4 1080 pixel;  2278, 1186
# Z5 1052 pixel;  2270, 1186
# Z6 1018 pixel;  2316, 1234
# Z7 1000 pixel;  2330, 1246
# Z8  994 pixel;  2570, 1832

import pandas as pd
import numpy as np
import csv

coord_zoom_data = {
    'Z1': {
        'dot': (2240, 1161),      
        'scale': 1.0       
    },
    'Z2': {
        'dot': (2240, 1161),
        'scale': 1.0
    },
    'Z3': {
        'dot': (2279, 1191),
        'scale': 1042/1063
    },
    'Z4': {
        'dot': (2278, 1186),
        'scale': 1042/1080
    },
    'Z5': {
        'dot': (2270, 1186),
        'scale': 1042/1052
    },
    'Z6': {
        'dot': (2316, 1234),
        'scale': 1042/1018
    },
    'Z7': {
        'dot': (2330, 1246),
        'scale': 1042/1000
    },
    'Z8': {
        'dot': (2570, 1832),
        'scale': 1042/994
    },
}

# === Choose a reference frame ===
reference_frame = 'Z1'
ref_dot = np.array(coord_zoom_data[reference_frame]['dot'])
ref_scale = coord_zoom_data[reference_frame]['scale']

ellipses_df = pd.read_csv('path_to_csv_containing_fitted_ellipses_data')

# === Transform function ===
def transform_ellipse(X_coord, Y_coord, Maj_ax_Length, Min_ax_Length, Angle, scale, dot, ref_dot):
    # Translate to origin based on dot, then scale
    rel = np.array([X_coord, Y_coord]) - np.array(dot)
    scale_factor = ref_scale / scale
    rel_scaled = rel * scale_factor

    # Translate back to reference space
    aligned = rel_scaled + ref_dot

    # Scale axes
    a_aligned = Maj_ax_Length * scale_factor
    b_aligned = Min_ax_Length * scale_factor

    return aligned[0], aligned[1], a_aligned, b_aligned, Angle

# === Process all ellipsoids ===
aligned_rows = []

for _, row in ellipses_df.iterrows():
    frame = row['frame']
    x, y, a, b, angle = row[['X_coord', 'Y_coord', 'Maj_ax_Length', 'Min_ax_Length', 'Angle']]

    dot = coord_zoom_data[frame]['dot']
    scale = coord_zoom_data[frame]['scale']

    new_x, new_y, new_a, new_b, new_angle = transform_ellipse(x, y, a, b, angle, scale, dot, ref_dot)

    scale_factor = ref_scale / scale
    length = row['Lenghts (m)'] * scale_factor
    velocity = row['Velocities (m/s)'] * scale_factor
    level = row['Z_level']

    aligned_rows.append([
        frame, new_x, new_y, new_a, new_b, new_angle, length, velocity, level
    ])

df_aligned = pd.DataFrame(aligned_rows, columns=["frame", "x", "y", "a", "b", "angle", "length", "velocity", "level"])
df_aligned.to_csv('path_to_csv_file_with_aligned_ellipses', index=False)