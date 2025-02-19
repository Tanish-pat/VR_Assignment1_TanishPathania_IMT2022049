# **VR_Assignment1_TanishPathania_IMT2022049**

## **Overview**
This repository contains two tasks:
1. **Coin Detection and Segmentation**
2. **Panorama Creation from Overlapping Images**

Each task is implemented in Python using **OpenCV, NumPy, and imutils** for image processing.

---

## **Installation & Dependencies**
Before running the scripts, install the required packages:
```bash
pip install -r requirements.txt
```
### **`requirements.txt` Includes:**
```
opencv-python
numpy
imutils
glob2
```

---

## **Repository Structure**
```
VR_Assignment1_TanishPathania_IMT2022049/
│── task1/                 # Coin Detection & Segmentation
│   ├── images/            # Input images (coins)
│   ├── outputs/           # Output images (segmented coins, detection)
│   ├── src/               # Code files
│   │   ├── main.py
│   │   ├── preprocessing.py
│   │   ├── segmentation.py
│
│── task2/                 # Image Stitching (Panorama Creation)
│   ├── images/            # Input images (overlapping scenes)
│   ├── output/            # Stitched outputs (stepwise panoramas, final panorama)
│   │   ├── panorama_final.jpg
│   │   ├── panoramas/
│   │   ├── keypoints/
│   ├── src/               # Code files
│   │   ├── feature_extraction.py
│   │   ├── load_images.py
│   │   ├── main.py
│   │   ├── post_processor.py
│   │   ├── stitcher.py
│
│── requirements.txt       # Dependencies
│── link.txt               # Github Link
│── README.md              # README file
```

---

## **1. Coin Detection & Segmentation**
### **Objective**
- Detect and segment Indian coins from an image.
- Count the total number of detected coins.

### **Steps & Methods Used**
1. **Preprocessing**
   - Convert image to **grayscale**
   - Apply **Gaussian blur** to remove noise
   - Use **Canny edge detection**
2. **Contour Detection**
   - Use `cv2.findContours()` to identify objects
   - Filter contours using **shape approximation**
3. **Segmentation & Counting**
   - Extract **individual coins** using bounding boxes
   - Save **segmented outputs**

### **Running the Code**
```bash
cd task1/src
python main.py
```
### **Observations for Task 1: Coin Detection & Segmentation**

This task involves detecting, segmenting, and counting coins in an image containing scattered Indian coins. The outputs generated during this process provide a comprehensive visualization of each step:

#### **1. Preprocessing Outputs**
- **Grayscale Image:** The input image is converted to grayscale to simplify processing and reduce computational complexity. This output helps visualize intensity variations in the image.
- **Blurred Image:** A Gaussian blur is applied to smoothen the image and reduce noise. This is crucial for avoiding false edge detections.
- **Edge Detection Output:** The Canny edge detection method highlights the strong edges in the image, helping to define the boundaries of the coins.

#### **2. Contour Detection Outputs**
- **Detected Contours Image (`detected_coins.jpg`)**
  - The algorithm detects coin-like contours and outlines them in **green** on the original image.
  - If a **non-circular object** is mistakenly detected, it is filtered out using contour approximation.
  - This step visually confirms which objects were recognized as coins.

#### **3. Segmentation Outputs**
- **Segmented Individual Coins (`segmented_coin_1.jpg`, `segmented_coin_2.jpg`, ... )**
  - Each detected coin is **isolated and saved separately** in `task1/outputs/`.
  - This helps validate if the algorithm correctly segments individual coins, even when they overlap slightly.

#### **4. Coin Counting Output**
- **Total Coins Count (Displayed in Console)**
  - The program prints the **total number of detected coins** in the console.
  - If coins are missing in the count, it indicates possible segmentation issues (e.g., overlapping coins being merged).

##### **Observations on Performance:**
✅ Successfully detects coins in well-lit images with clear separation.
✅ Handles **varying sizes** of coins effectively.
⚠️ **Overlapping coins** can sometimes merge, reducing count accuracy.
⚠️ Very **noisy backgrounds** (with other circular objects) may cause false detections.

---


### **Results**
- **Total Coins Detected:** ✅ *(Shown in console)*
- **Segmented Coins Saved:** `task1/outputs/`
- **Visual Output:** `task1/outputs/detected_coins.jpg`

---

## **2. Image Stitching (Panorama Creation)**
### **Objective**
- Create a **stitched panorama** from overlapping images.
- Extract **key points** and show **pairwise matches** before stitching.

### **Steps & Methods Used**
1. **Key Point Detection**
   - Use **SIFT** to extract key points
   - Match features using **FLANN-based matcher**
   - Save keypoint images for **debugging**
2. **Pairwise Stitching**
   - Use OpenCV’s **Stitcher API** to merge images
   - Perform **progressive stitching**
3. **Post-processing**
   - Crop **unnecessary black borders**
   - Save **intermediate panoramas**

### **Running the Code**
```bash
cd task2/src
python main.py
```

### **Results**
- **Key Points Saved in:** `task2/output/keypoints/`
- **Stepwise Panoramas Saved in:** `task2/output/panoramas/`
- **Final Panorama:** `task2/output/panorama_final.jpg`

---

### **Observations for Task 2: Image Stitching (Panorama Creation)**

This task involves stitching multiple overlapping images into a single panoramic view. The outputs generated at each step help visualize the **key points, pairwise image alignment, and final panorama creation.**

#### **1. Keypoint Detection & Matching Outputs**
- **Pairwise Keypoint Matching Images (`keypoints_1_2.jpg`, `keypoints_2_3.jpg`, … )**
  - The algorithm extracts **SIFT key points** from each pair of consecutive images.
  - It then **matches key points** using a FLANN-based matcher.
  - The **good matches** are visualized with colored lines connecting similar features between two images.
  - This step helps validate whether the images have **sufficient feature overlap** for stitching.

#### **2. Stepwise Panorama Outputs**
- **Intermediate Panoramas (`panorama_1_2.jpg`, `panorama_2_3.jpg`, … )**
  - The stitching process is done **progressively**, meaning that each pair of images is merged before moving to the next.
  - These intermediate results are stored in `task2/output/panoramas/`.
  - If the alignment in an intermediate panorama is incorrect, it means the feature matching was inaccurate or the images did not overlap well.

#### **3. Final Stitched Panorama Output**
- **Final Panorama (`panorama_final.jpg`)**
  - After merging all images, the final **stitched panorama** is generated and stored in `task2/output/`.
  - The program **removes black borders** from the stitched image to improve the visual output.
  - If an error occurs, it usually means that there wasn’t enough feature overlap between images.

##### **Observations on Performance:**
✅ Stitching works well when images have **sufficient overlap** and are taken from a **consistent perspective**.
✅ The progressive panorama generation allows **debugging** alignment issues at each step.
✅ **Black border removal** improves the final output.
⚠️ If images lack **enough distinct features**, keypoint detection may fail, and stitching won’t work.
⚠️ **Extreme perspective shifts** between images may cause distortions in the final panorama.

---
