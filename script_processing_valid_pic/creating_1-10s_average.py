# CREATING 1/10s AVERAGE 

import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt

########## FOR SHOWING PICTURE ##################
def show_image(title, image):
    if image.dtype == bool:
        image = image.astype(np.uint8) * 255
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    elif len(image.shape) == 3:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()
#################################################


# Load all image paths
image_paths = glob.glob("path_to_masked_1/10s_pics")  # Change this to match your files

# Initialize accumulator with zeros
average_img = None
count = 0

# Loop through all images and accumulate pixel values
for path in image_paths:
    img = cv2.imread(path).astype(np.float32)  # Load as float32 for precision
    if average_img is None:
        average_img = img
    else:
        average_img += img
    count += 1

# Divide by number of images to get the average
average_img /= count

# Convert to uint8 and save/show
average_img = np.clip(average_img, 0, 255).astype(np.uint8)
show_image("Average Image", average_img)
cv2.imwrite('path_to_saved_average_1/10s_pic', average_img)