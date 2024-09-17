import cv2
import time
import imutils

# Use camera index 0
cam = cv2.VideoCapture(0)

# Allow the camera to warm up
time.sleep(1)

# Initialize variables
firstFrame = None  # Variable to store the first frame for motion detection
area = 500  # Minimum contour area to be considered as a moving object

# Main loop for capturing and processing frames
while True:
    # Capture a frame from the camera
    ret, img = cam.read()

    # Check if frame is captured successfully
    if not ret:
        print("Error: Unable to capture frame")
        break

    text = "Normal"  # Default text to display on the frame
    img = imutils.resize(img, width=500)  # Resize the frame to a smaller width for faster processing

    # Convert the frame to grayscale
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise in the frame
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)

    # If it's the first frame, store it for motion detection
    if firstFrame is None:
        firstFrame = gaussianImg
        continue

    # Compute the absolute difference between the current frame and the first frame
    imgDiff = cv2.absdiff(firstFrame, gaussianImg)

    # Threshold the difference image to obtain a binary image
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]

    # Apply dilation to the thresholded image to fill in gaps
    threshImg = cv2.dilate(threshImg, None, iterations=2)

    # Find contours in the thresholded image
    try:
        (cnts, _) = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    except ValueError:
        (_, cnts, _) = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If no contours are found, continue to the next iteration
    if len(cnts) == 0:
        continue

    # Loop over the contours
    for c in cnts:
        # If the contour area is smaller than the specified area, skip it
        if cv2.contourArea(c) < area:
            continue
        # Compute the bounding box for the contour
        (x, y, w, h) = cv2.boundingRect(c)
        # Draw a rectangle around the moving object
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object detected"  # Update text if a moving object is detected

    print(text)  # Print the status of the detection
    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)  # Draw text on the frame
    cv2.imshow("cameraFeed", img)  # Display the frame
    key = cv2.waitKey(1) & 0xFF  # Wait for a key press
    if key == ord("q"):  # If 'q' is pressed, exit the loop
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
