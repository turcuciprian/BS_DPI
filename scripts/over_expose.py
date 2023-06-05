import os
from PIL import Image
from PIL import ImageEnhance
from lib.paths import root_before, root_after, folder_name_over_expose
from lib.main import *

def over_expose_images(source_folder, destination_folder, times_to_expose):
    # Check if the destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get a list of all files in the source folder
    file_list = os.listdir(source_folder)

    for filename in file_list:
        # Avoid non jpg or png files
        if not is_image(filename):
            continue 
        # Check if the file is an image (assuming all image files have extensions)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Open the image
            image_path = os.path.join(source_folder, filename)
            image = Image.open(image_path)

            # Apply overexposure to the image
            enhancer = ImageEnhance.Brightness(image)
            overexposed_image = enhancer.enhance(times_to_expose)  # Increase the brightness, adjust the value as needed

            # Save the overexposed image to the destination folder
            destination_path = os.path.join(destination_folder, filename)
            overexposed_image.save(destination_path)

            print(f"Processed: {filename}")

    print("Overexposure process complete.")

# Example usage
# overexpose_images('source_folder_path', 'destination_folder_path',2)

# Example:
# over_expose_images(root_before, os.path.join(root_after,folder_name_over_expose),2)
