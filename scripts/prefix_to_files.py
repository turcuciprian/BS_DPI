import os
import shutil

def add_prefix_to_files(first_folder_source_path, second_folder_source_path, output_folder_path):
    # Rename files in the first folder
    first_folder_name = os.path.basename(os.path.normpath(first_folder_source_path))
    for root, _, files in os.walk(first_folder_source_path):
        for file_name in files:
            source_file_path = os.path.join(root, file_name)
            new_file_name = first_folder_name + "_" + file_name
            destination_file_path = os.path.join(output_folder_path, new_file_name)
            shutil.copy2(source_file_path, destination_file_path)

    # Rename files in the second folder
    for root, _, files in os.walk(second_folder_source_path):
        for file_name in files:
            source_file_path = os.path.join(root, file_name)
            new_file_name = first_folder_name + "_" + file_name
            destination_file_path = os.path.join(output_folder_path, new_file_name)
            shutil.copy2(source_file_path, destination_file_path)


# # Example usage
# first_folder_path = "/path/to/first_folder"
# second_folder_path = "/path/to/second_folder"
# output_folder_path = "/path/to/output_folder"

# add_prefix_to_files(first_folder_path, second_folder_path, output_folder_path)