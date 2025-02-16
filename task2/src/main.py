import cv2
import os
import glob
from load_images import load_images
from feature_extraction import extract_features, match_features, draw_keypoints
from stitcher import stitch_pair
from post_processor import post_process_stitched_image

# Define input and output folders
input_folder = "../images"
output_folder = "../output"
panoramas_folder = os.path.join(output_folder, "panoramas")
keypoints_folder = os.path.join(output_folder, "keypoints")
final_panorama_path = os.path.join(output_folder, "panorama_final.jpg")

# Ensure output folders exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(panoramas_folder, exist_ok=True)
os.makedirs(keypoints_folder, exist_ok=True)

# Load images
image_paths = glob.glob(os.path.join(input_folder, "*.jpg"))
image_paths.sort()  # Ensure correct order
images = [cv2.imread(img) for img in image_paths]

if len(images) < 2:
    print("Need at least two images for stitching. Exiting...")
    exit()

# Stitch images step by step
current_panorama = images[0]

for i in range(1, len(images)):
    img1, img2 = current_panorama, images[i]

    # Extract keypoints
    keypoints1, des1 = extract_features(img1)
    keypoints2, des2 = extract_features(img2)

    # Match features
    matches = match_features(img1, img2, des1, des2)

    # Save keypoint matches
    keypoint_match_path = os.path.join(keypoints_folder, f"keypoints_{i}_{i+1}.jpg")
    draw_keypoints(img1, img2, keypoints1, keypoints2, matches, keypoint_match_path)
    print(f"Keypoints match saved: {keypoint_match_path}")

    # Stitch the pair
    stitched_img = stitch_pair(img1, img2)

    if stitched_img is None:
        print(f"Stitching failed for images {i} and {i+1}.")
        continue

    # Crop black borders
    stitched_img = post_process_stitched_image(stitched_img)

    # Save intermediate panorama
    panorama_step_path = os.path.join(panoramas_folder, f"panorama_{i}_{i+1}.jpg")
    cv2.imwrite(panorama_step_path, stitched_img)
    print(f"Stepwise Panorama saved: {panorama_step_path}")

    # Update current panorama for next step
    current_panorama = stitched_img

# Save final panorama
cv2.imwrite(final_panorama_path, current_panorama)
print(f"Final panorama saved at {final_panorama_path}")
