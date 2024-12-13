import os
import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor

def process_image(image_path, output_folder, size=(128, 128)):
    try:
        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error reading image: {image_path}")
            return

        # Resize the image
        resized_image = cv2.resize(image, size)

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        # Save the processed image
        output_path = os.path.join(output_folder, os.path.basename(image_path))
        cv2.imwrite(output_path, gray_image)
        print(f"Processed and saved: {output_path}")
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")

def batch_process_images(input_folder, output_folder, size=(128, 128)):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # List all images in the input folder
    image_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    print(f"Found {len(image_files)} images to process.")

    # Use ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor() as executor:
        for image_path in image_files:
            executor.submit(process_image, image_path, output_folder, size)

if __name__ == "__main__":
    # Example usage
    input_folder = "input_images"  # Replace with the path to your input images folder
    output_folder = "output_images"  # Replace with the path to your output folder
    batch_process_images(input_folder, output_folder)
