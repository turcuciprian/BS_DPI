import os
from PIL import Image
from lib.paths import root_before, root_after, folder_name_resized
from lib.main import *

def resize_and_crop_images(input_path, output_path, size):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Get a list of input files
    files = os.listdir(input_path)

    for filename in files:
        # Avoid non jpg or png files
        if not is_image(filename):
            continue 
        # Create input and output file paths
        input_file = os.path.join(input_path, filename)
        output_file = os.path.join(output_path, filename)

        # Open the input image
        image = Image.open(input_file)
        
        # ---
        # Calculate aspect ratio.
        w, h = image.size
        width, crop_height = size
        aspect_ratio = h / w

        # Calculate new height maintaining aspect ratio.
        new_height = int(width * aspect_ratio)

        # Resize the image.
        image = image.resize((width, new_height))

        # Calculate position for cropping.
        left = 0
        top = (new_height - crop_height) / 2
        right = width
        bottom = (new_height + crop_height) / 2

        # Crop the image.
        resized_image = image.crop((left, top, right, bottom))
        # ---

        # Resize and crop the image
        resized_image = image.resize(size, Image.ANTIALIAS)

        # Save the resized and cropped image
        resized_image.save(output_file)

    print("Images resized and cropped successfully.")

#
# Usage example:
# 

# input_folder = "path/to/input/folder"
# output_folder = "path/to/output/folder"
# image_size = (300, 200)

# resize_and_crop_images(input_folder, output_folder, image_size)
