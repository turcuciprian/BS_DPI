from PIL import Image
import numpy as np
import os
from lib.main import *
from lib.paths import root_before, root_after, folder_name_mask

# Set the input and output folder paths
input_folder = root_before
output_folder = os.path.join(root_after, folder_name_mask)

# Define the color threshold (in RGB)
red_threshold = (255, 0, 0)
color_threshold = 50

# Iterate through each file in the input folder
for filename in os.listdir(input_folder):
    # Avoid non jpg or png files
    if not is_image(filename):
        continue
    # Open the image
    image_path = os.path.join(input_folder, filename)
    image = Image.open(image_path)

    # Get the pixel data
    pixel_data = image.load()

    # Iterate through each pixel in the image
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            # Check if the pixel is approximately red
            if (
                pixel_data[i, j][0] >= red_threshold[0] - color_threshold
                and pixel_data[i, j][1] <= red_threshold[1] + color_threshold
                and pixel_data[i, j][2] <= red_threshold[2] + color_threshold
            ):
                # Replace approximately red pixels with #FFFFFF mask color
                pixel_data[i, j] = (255, 255, 255)
            else:
                # Replace other colored pixels with white
                pixel_data[i, j] = (0, 0, 0)
    file_extension = os.path.splitext(filename)[1]
    # create the new file name with the suffix "_mask"
    new_file_name = filename.replace(file_extension, "") + "_mask.png"
    print(new_file_name)
    # Save the new image in the output folder
    output_path = os.path.join(output_folder, new_file_name)
    image.save(output_path, quality=100, optimize=False)
