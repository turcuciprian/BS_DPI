from PIL import Image
import os
from lib.main import *
from lib.paths import root_before, root_after, folder_name_greyscale


def greyscale(source_folder, destination_folder):
    # Set the input and output folder paths
    input_folder = source_folder

    # Iterate through each file in the input folder
    for filename in os.listdir(source_folder):
        # Avoid non jpg or png files
        if not is_image(filename):
            continue

        # Open the image
        image_path = os.path.join(source_folder, filename)
        image = Image.open(image_path)

        # # Convert the image to greyscale with image mode rgb
        # Convert the image to black and white
        image = image.convert("L")
        # Convert the image back to RGB mode
        image = image.convert("RGB")

        # Save the black and white image in the output folder
        output_path = os.path.join(destination_folder, filename)
        image.save(output_path)
