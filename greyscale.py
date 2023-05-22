from PIL import Image
import os
from myLib import *
from paths import root_before, root_after, folder_name_greyscale


# Set the input and output folder paths
input_folder = os.path.join(root_before,folder_name_greyscale)
output_folder = os.path.join(root_after,folder_name_greyscale)
create_folder_if_missing(input_folder)
create_folder_if_missing(output_folder)

# Iterate through each file in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Open the image
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)
        
        # # Convert the image to greyscale with image mode rgb  
        # Convert the image to black and white
        image = image.convert('L')
        
        # Convert the image back to RGB mode
        image = image.convert('RGB')
        
        # Save the black and white image in the output folder
        output_path = os.path.join(output_folder, filename)
        image.save(output_path)