import os
from PIL import Image
from PIL import ImageEnhance
from lib.paths import root_before, root_after, folder_name_darken

def darken_images(source_folder, destination_folder, percentage_to_darken):

    # Get a list of all files in the source folder
    file_list = os.listdir(source_folder)

    for file_name in file_list:
        # Check if the file is an image (assuming all image files have extensions)
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Open the image
            image_path = os.path.join(source_folder, file_name)
            image = Image.open(image_path)

            # Apply darkening to the image
            enhancer = ImageEnhance.Brightness(image)
            darkened_image = enhancer.enhance(percentage_to_darken)  # Decrease the brightness, adjust the value as needed

            # Save the darkened image to the destination folder
            destination_path = os.path.join(destination_folder, file_name)
            darkened_image.save(destination_path)

            print(f"Processed: {file_name}")

    print("Darkening process complete.")

# Example usage
# darken_images("path/to/source/folder", "path/to/destination/folder",0.5)

darken_images(root_before, os.path.join(root_after,folder_name_darken),0.5)

