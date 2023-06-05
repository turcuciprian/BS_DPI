import os
import shutil
from lib.main import *


def prefix_and_gather_recursively(
    first_folder_source_path,
    second_folder_source_path,
    output_first_folder_path,
    output_second_folder_path,
):
    # Rename files in the first folder
    first_folder_name = os.path.basename(os.path.normpath(first_folder_source_path))
    for root, _, files in os.walk(first_folder_source_path):
        for filename in files:
            # Avoid non jpg or png files
            if not is_image(filename):
                continue
            source_file_path = os.path.join(root, filename)
            new_file_name = first_folder_name + "_" + filename
            destination_file_path = os.path.join(
                output_first_folder_path, new_file_name
            )
            dest = shutil.copy2(source_file_path, destination_file_path)
            print("gathered: " + dest)

    # Rename files in the second folder
    for root, _, files in os.walk(second_folder_source_path):
        for filename in files:
            # Avoid non jpg or png files
            if not is_image(filename):
                continue
            # Avoid non jpg or png files
            if not is_image(filename):
                continue
            source_file_path = os.path.join(root, filename)
            new_file_name = first_folder_name + "_" + filename
            destination_file_path = os.path.join(
                output_second_folder_path, new_file_name
            )
            shutil.copy2(source_file_path, destination_file_path)


# # Example usage
# first_folder_path = "/path/to/first_folder"
# second_folder_path = "/path/to/second_folder"
# output_folder_path = "/path/to/output_folder"

# prefix_and_gather_recursively(first_folder_path, second_folder_path, output_folder_path)
