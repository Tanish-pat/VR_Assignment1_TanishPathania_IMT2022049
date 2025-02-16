import cv2
import glob
import os

def load_images(image_folder):
    """
    Loads all images from the specified folder.
    """
    image_paths = sorted(glob.glob(os.path.join(image_folder, "*.jpg")))
    images = [cv2.imread(img) for img in image_paths]

    if not images:
        print("No images found in the folder!")

    return images
