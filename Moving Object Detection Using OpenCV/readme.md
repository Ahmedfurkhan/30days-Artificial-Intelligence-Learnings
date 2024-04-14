# Moving Object Detection using OpenCV

This repository contains Python code for detecting moving objects using OpenCV, a popular computer vision library. The code detects moving objects in a video stream or recorded video file and outlines them in a bounding box.

## Dependencies

- Python 3.x
- OpenCV
    ```bash
    pip install opencv-python
- imutils
    ```bash
    pip install immutils

You can install the required Python libraries using pip:
pip install opencv-python imutils


## Usage

1. Clone the repository:
   
   ```bash
   git clone https://github.com/your-username/moving-object-detection.git
   cd moving-object-detection


1. Run the main Python script: `Moving Object camera test.py`

The script will capture video from your default camera and display the moving objects with bounding boxes in real-time.

## How it works

The main steps involved in moving object detection using OpenCV are as follows:

### 1. Resizing the Image

Before processing, the input image or video frame is resized to a smaller size using the `imutils.resize()` function. Resizing the image helps in improving processing speed and reducing computational load.

### 2. Gaussian Blur

The resized image is passed through a Gaussian blur filter using the `cv2.GaussianBlur()` function. Gaussian blur helps in reducing noise and smoothing out the image, which can improve the accuracy of subsequent processing steps.

### 3. Thresholding

After blurring, the image is thresholded to create a binary image using the `cv2.threshold()` function. Thresholding converts the grayscale image into a binary image where pixels are classified as either foreground (moving objects) or background (static elements).

### 4. Motion Detection

Once the thresholded image is obtained, contours are extracted using the `cv2.findContours()` function. Contours represent the boundaries of objects in the image. By analyzing the contours, moving objects can be detected and outlined with bounding boxes using the `cv2.rectangle()` function.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or submit a pull request.
