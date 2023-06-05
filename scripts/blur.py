import cv2
import os
from lib.main import *

def blur_images(input_folder, output_folder, blur_percentage):
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate over every file in the input directory
    for filename in os.listdir(input_folder):
        # Avoid non jpg or png files
        if not is_image(filename):
            continue
        # Make sure the file is an image (you may need to adjust this depending on your image types)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            # Read the image
            img = cv2.imread(os.path.join(input_folder, filename))

            # Calculate the blur radius (must be odd)
            blur_radius = max(1, round(blur_percentage * img.shape[1] // 2 * 2 + 1))
            
            # Blur the image
            img = cv2.GaussianBlur(img, (blur_radius, blur_radius), 0)

            # Write the image to the output directory
            cv2.imwrite(os.path.join(output_folder, filename), img)

# blur_images('path/to/input/folder', 'path/to/output/folder', 0.1)
#