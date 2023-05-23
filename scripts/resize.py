import os
from PIL import Image
from paths import root_before, root_after, folder_name_resize

def resize_and_crop_images(input_path, output_path, size):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Get a list of input files
    files = os.listdir(input_path)

    for file_name in files:
        # Create input and output file paths
        input_file = os.path.join(input_path, file_name)
        output_file = os.path.join(output_path, file_name)

        # Open the input image
        image = Image.open(input_file)

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

# using it:

input_folder =root_before
output_folder =os.path.join(root_after, folder_name_resize)
image_size = (800, 600)

resize_and_crop_images(input_folder, output_folder, image_size)
