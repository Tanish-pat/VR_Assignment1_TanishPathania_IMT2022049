import cv2
import numpy as np
import os

def extract_features(image):
    """
    Extracts key points and descriptors from an image using SIFT.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(gray, None)
    return keypoints, descriptors

def match_features(image1, image2, des1, des2):
    """
    Matches features between two images using FLANN-based matcher.
    """
    index_params = dict(algorithm=1, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1, des2, k=2)

    # Apply Lowe’s ratio test
    good_matches = [m for m, n in matches if m.distance < 0.75 * n.distance]

    return good_matches

def draw_keypoints(image1, image2, keypoints1, keypoints2, matches, output_path):
    """
    Draws keypoint matches between two images and saves the result.
    """
    matched_image = cv2.drawMatches(image1, keypoints1, image2, keypoints2, matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv2.imwrite(output_path, matched_image)
