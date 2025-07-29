import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.cm import ScalarMappable
from creating_color_map import extract_colormap_from_image
from matplotlib.colors import Normalize
import os

df_tot = pd.read_csv('path_to_alignes_ellipses_csv')

output_folder = 'path_to_output_folder'
os.makedirs(output_folder, exist_ok=True) 

image_path = 'path_to_colorbar_image'
cmap = extract_colormap_from_image(image_path)
norm = Normalize(vmin=0, vmax=0.5)
#norm = Normalize(vmin=0, vmax=0.75)

# === Parameters for ellipsoid appearance ===
width = 1  # minor axis length
height = 25.0  # major axis length

# === Loop over unique frames ===
for frame_id in df_tot['frame'].unique():
    df_frame = df_tot[df_tot['frame'] == frame_id]

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_facecolor('black')
    sm = ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    # Plot ellipsoids
    for idx, row in df_frame.iterrows():
        x, y = row['x'], row['y']
        angle = row['angle']
        velocity = row['velocity']
        color = cmap(norm(velocity))

        ell = Ellipse((x, y), width=width, height=height, angle=angle, color=color, alpha=1)
        ax.add_patch(ell)

    ax.set_aspect('equal')
    plt.xlabel('X', fontsize=20, weight='bold', labelpad=5)
    plt.ylabel('Y', fontsize=20, weight='bold', labelpad=5)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    ax.set_xlim(df_frame['x'].min() - 50, df_frame['x'].max() + 50)
    ax.set_ylim(df_frame['y'].min() - 50, df_frame['y'].max() + 50)
    ax.invert_xaxis()
    plt.grid(False)

    # Save plot 
    output_path = os.path.join(output_folder, f"ellipsoids_{frame_id}_0.5.svg")
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.show(block=True)
