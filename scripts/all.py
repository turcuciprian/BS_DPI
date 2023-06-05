import os
from create_folders import create_folders
from resize import resize_and_crop_images
from greyscale import greyscale
from darken import darken_images
from over_expose import over_expose_images
from blur import blur_images
from noise import add_noise_to_images
from lib.paths import root_before, root_after, folder_name_resized, folder_name_greyscale, folder_name_darken, folder_name_blur,folder_name_noise, folder_name_over_expose

# 
#  1. Create the destination folders
# 
create_folders()

# 
#  2. Resize and crop originals
# 

# prep
input_folder =root_before
resized_output_folder =os.path.join(root_after, folder_name_resized)
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
greyscale(greyscale_input_folder, greyscale_output_folder)

# 
#  4. Darken resized
# 

# prep
darken_input_folder =resized_output_folder
darken_output_folder =os.path.join(root_after, folder_name_darken)

# process
darken_images(darken_input_folder, darken_output_folder,0.5)

# 
#  5. Over Expose Resized
# 

# prep
over_expose_input_folder =resized_output_folder
over_exposed_output_folder =os.path.join(root_after, folder_name_over_expose)

# process
over_expose_images(over_expose_input_folder, over_exposed_output_folder,2)

# 
#  6. Blur Resized
# 

# prep
blur_input_folder =resized_output_folder
blur_output_folder =os.path.join(root_after, folder_name_blur)

# process
blur_images(blur_input_folder, blur_output_folder,0.02)

# 
#  7. Noise Resized
# 

# prep
noise_input_folder =resized_output_folder
noise_output_folder =os.path.join(root_after, folder_name_noise)

# process
add_noise_to_images(noise_input_folder, noise_output_folder,70)
