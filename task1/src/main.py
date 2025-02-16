import cv2
import os
import glob
from preprocessing import preprocess_image
from segmentation import detect_coins, segment_coins, count_coins

# Input and Output directories
input_folder = "../images"
output_folder = "../outputs"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get all image paths in the folder
image_paths = glob.glob(os.path.join(input_folder, "*.jpeg"))  # Change extension if needed

# Process each image
for image_path in image_paths:
    # Extract image filename (without extension) to create a corresponding output folder
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    image_output_folder = os.path.join(output_folder, image_name)
    image_output_folder = image_output_folder + "_output"
    # Create folder for the specific image's outputs
    os.makedirs(image_output_folder, exist_ok=True)

    # Process the image
    image, gray, edges = preprocess_image(image_path)
    contours = detect_coins(image, edges)
    segment_coins(image, contours, image_output_folder)

    # Draw contours on the original image and save the result
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    cv2.imwrite(os.path.join(image_output_folder, "detected_coins.jpg"), image)

    # Print the count of detected coins
    print(f"Image: {image_name}, Total Coins Detected: {count_coins(contours)}")
