# Object Tracking Based On Color

This Python script utilizes Tkinter for the graphical user interface and OpenCV for image processing to perform color-based object tracking.

## Installation

1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Install the required Python libraries using pip:

pip install numpy opencv-python Pillow pyautogui


## Usage

1. Clone this repository to your local machine:
git clone https://github.com/Ahmedfurkhan/30days-Artificial-Intelligence-Learnings.git

2. Navigate to the project directory:
cd Object-Tracking-Based-On-Color

3. Run the script:
python colorCalibrationforHSV.py

## Explanation

### Main Script (colorCalibrationforHSV.py)

- The script provides a graphical user interface for adjusting HSV color ranges and performing color-based object tracking.
- It uses Tkinter for the GUI and OpenCV for image processing.
- The `App` class represents the application, which includes sliders for adjusting HSV values, buttons for presets and actions, and image display areas.
- Methods like `open_file`, `preset_r`, `preset_g`, and `preset_b` handle file opening and presetting color ranges.
- The `show_changes` method updates the displayed images based on HSV slider values.
- The `take_screenshot` method captures a screenshot using PyAutoGUI, and the `resize_image` method resizes images as needed.
- The `print_img_array` method is intended to print the image array but currently incomplete.


