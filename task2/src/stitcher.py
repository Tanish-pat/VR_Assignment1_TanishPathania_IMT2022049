import cv2
import os

def stitch_pair(image1, image2):
    """
    Stitches two images into a single panorama.
    """
    stitcher = cv2.Stitcher_create()
    error, stitched_img = stitcher.stitch([image1, image2])

    if error == cv2.Stitcher_OK:
        return stitched_img
    else:
        print("Error during stitching two images.")
        return None
