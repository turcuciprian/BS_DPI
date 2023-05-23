import os
from create_folders import create_folders
from resize import resize_and_crop_images
from greyscale import greyscale
from darken import darken_images
from over_expose import over_expose_images
from lib.paths import root_before, root_after, folder_name_resize, folder_name_greyscale, folder_name_darken

# 
#  1. Create the destination folders
# 
create_folders()

# 
#  2. Resize and crop originals
# 

# prep
input_folder =root_before
resized_output_folder =os.path.join(root_after, folder_name_resize)
image_size = (800, 600)

# process
resize_and_crop_images(input_folder, resized_output_folder, image_size)

# 
#  3. Greyscale resized
# 

# prep
greyscale_input_folder =resized_output_folder
greyscale_output_folder =os.path.join(root_after, folder_name_greyscale)

# process
greyscale(input_folder, greyscale_output_folder)

# 
#  4. Darken resized
# 

# prep
darken_input_folder =resized_output_folder
darken_output_folder =os.path.join(root_after, folder_name_darken)

# process
darken_images(input_folder, darken_output_folder,0.5)

# 
#  5. Over Expose Resized
# 

# prep
over_expose_input_folder =resized_output_folder
over_exposed_output_folder =os.path.join(root_after, over_expose_input_folder)

# process
over_expose_images(input_folder, over_exposed_output_folder,2)
