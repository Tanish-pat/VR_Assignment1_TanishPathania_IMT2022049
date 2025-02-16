import cv2

def detect_coins(image, edges):
    dilated = cv2.dilate(edges, (1, 1), iterations=2)
    contours, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    coin_contours = []
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) > 5:  # Filtering out non-circular objects
            coin_contours.append(contour)

    return coin_contours

def segment_coins(image, contours, output_folder="outputs/"):
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        coin_segment = image[y:y+h, x:x+w]
        cv2.imwrite(f"{output_folder}/segmented_coin_{i+1}.jpg", coin_segment)

def count_coins(contours):
    return len(contours)
