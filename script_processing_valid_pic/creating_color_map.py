from PIL import Image
import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def extract_colormap_from_image(image_path):
    
    img = Image.open(image_path).convert("RGB")
    img_np = np.array(img)

    # Find the row with the highest color variation
    variances = [np.std(img_np[row], axis=0).mean() for row in range(img_np.shape[0])]
    best_row_idx = np.argmax(variances)
    color_row = img_np[best_row_idx]

    # Convert to array of RGB tuples
    colors_arr = np.array([tuple(pixel) for pixel in color_row])
    x_original = np.linspace(0, 1, len(colors_arr))
    x_new = np.linspace(0, 1, 256)

    # Interpolate R, G, B channels separately
    interp_r = interp1d(x_original, colors_arr[:, 0], kind='linear')
    interp_g = interp1d(x_original, colors_arr[:, 1], kind='linear')
    interp_b = interp1d(x_original, colors_arr[:, 2], kind='linear')

    r_new = interp_r(x_new)
    g_new = interp_g(x_new)
    b_new = interp_b(x_new)

    # Stack and normalize to [0, 1]
    interp_colors = np.vstack([r_new, g_new, b_new]).T / 255.0

    # Apply your manual color fix
    interp_colors[156] = [1, 0.670842, 0.215686]
    interp_colors = interp_colors[29:220]  # Crop relevant part

    # Build and return colormap
    custom_cmap = ListedColormap(interp_colors)
    return custom_cmap


# Example usage:
if __name__ == "__main__":
    image_path = 'path_to_image_with_colorbar'
    cmap = extract_colormap_from_image(image_path)

    # Preview for debugging
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    plt.imshow(gradient, aspect='auto', cmap=cmap)
    plt.axis('on')
    plt.title("Extracted Colormap from Image")
    plt.show()