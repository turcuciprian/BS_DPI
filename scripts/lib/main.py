import os


def create_folder_if_missing(folder_name):
    # Create a folder if it doesn't exist
    folderExists = os.path.exists(folder_name)
    if not folderExists:
        # Create a new directory because it does not exist
        os.makedirs(folder_name)


def is_image(filename):
    return filename.lower().endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif"))
