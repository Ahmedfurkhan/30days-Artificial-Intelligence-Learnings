# Face Detection and Database Creation

This repository contains code for detecting faces using OpenCV with Haar cascade classifier and creating a database of face images for training machine learning models.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Ahmedfurkhan/30days-Artificial-Intelligence-Learnings.git
    cd Face Detection & Algorithms
    ```

2. **Install dependencies:**

    Make sure you have Python and pip installed on your system. Then, install the required Python packages using pip:

    ```bash
    pip install opencv-python
    pip install datasets
    ```

3. **Download the Haar cascade file:**

    Download the Haar cascade file named `haarcascade_frontalface_default.xml` from the OpenCV GitHub repository or other reliable sources. You can also use `haarcascade_frontalface_default.xml` provided by OpenCV.

5. **Run the script:For Creating Database**
   
   ```bash
    python faceDataset.py
    ```

6. **Run the script:For Capturing Pic**

    ```bash
    python FaceDetection.py
    ```

## Usage

1. **Face Detection:**

    The `face_detection.py` script captures video from the default camera on your system and detects faces in real-time using OpenCV's Haar cascade classifier (`haarcascade_frontalface_default.xml`).

2. **Database Creation:**

    The script can also be used to create a database of face images for training machine learning models for face recognition. After detecting faces, it captures multiple images of each face and saves them in a specified directory for further processing.

3. **Customization:**

    You can customize the script by adjusting parameters such as camera index, image dimensions, and cascade file path (`haarcascade_frontalface_default.xml`) to suit your requirements.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.


