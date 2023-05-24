import os
import cv2
import numpy as np

def add_noise_to_images(input_folder, output_folder, noise_percentage):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    # Process each image file
    for filename in image_files:
        # Load the image
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        # Add noise to the image
        noise = np.random.normal(0, noise_percentage, image.shape)
        noisy_image = image + noise

        # Ensure pixel values are within 0-255 range
        noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

        # Save the noisy image to the output folder
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, noisy_image)

        print(f"Noise added to {filename} and saved as {output_path}")

# # Example usage
# input_folder = "path/to/input/folder"
# output_folder = "path/to/output/folder"
# noise_percentage = 10  # 10% noise
# add_noise_to_images(input_folder, output_folder, noise_percentage)
