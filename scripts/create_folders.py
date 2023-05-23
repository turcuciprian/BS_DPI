import os
from lib.paths import root_before, root_after, folder_name_blur, folder_name_greyscale, folder_name_mask, folder_name_noise, folder_name_resize,folder_name_over_expose, folder_name_darken



# list of folders to generate
list_of_folders = [folder_name_blur, folder_name_greyscale, folder_name_mask, folder_name_noise, folder_name_resize,folder_name_over_expose, folder_name_darken]

# create base root folders if they don't exist
os.makedirs(root_before,exist_ok=True)
os.makedirs(root_after,exist_ok=True)
# cycle trought the list of folder names to create    
for folder in list_of_folders:
    # create a child folder for after root path - as a string
    after_full_path = os.path.join(root_after, folder)
    # create after full path child folder string name
    os.makedirs(after_full_path,exist_ok=True)