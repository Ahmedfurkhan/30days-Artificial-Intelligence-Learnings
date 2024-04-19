import cv2
import numpy as np

# Define the color ranges for different objects
color_ranges = {
    "green": (np.array([30, 50, 50]), np.array([90, 255, 255])),   # Green
    "red": (np.array([0, 50, 50]), np.array([10, 255, 255]))       # Red (wrap around hue range)
}

# Start capturing video from the camera
camera = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = camera.read()
    
    # Resize the frame to a smaller size for faster processing
    frame = cv2.resize(frame, (600, 400))
    
    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Perform color segmentation to detect the object
    mask = cv2.inRange(hsv, color_ranges["green"][0], color_ranges["green"][1])  # Change "green" to the desired color
    
    # Perform morphological operations to remove noise and refine the mask
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Check if any contours were found
    if len(contours) > 0:
        # Find the largest contour (assuming the largest contour corresponds to the object)
        c = max(contours, key=cv2.contourArea)
        
        # Get the center and radius of the enclosing circle of the largest contour
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))
        
        # Draw the enclosing circle and centroid on the frame
        cv2.circle(frame, center, int(radius), (0, 255, 255), 2)
        cv2.circle(frame, center, 5, (0, 0, 255), -1)
        
        # Print the position and size of the object
        print("Position:", center, "Radius:", radius)
    
    # Display the frame
    cv2.imshow("Frame", frame)
    
    # Check for key press and break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
