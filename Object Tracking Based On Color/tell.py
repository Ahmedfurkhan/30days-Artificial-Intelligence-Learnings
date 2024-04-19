import cv2
import numpy as np

# Define the lower and upper bounds for the color you want to track
color_ranges = {
    "green": (np.array([30, 50, 50]), np.array([90, 255, 255])),   # Green
    "red": (np.array([0, 50, 50]), np.array([10, 255, 255]))       # Red (wrap around hue range)
}

# Function to track the object of a specific color
def track_object(color):
    # Start the camera
    camera = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        grabbed, frame = camera.read()
        if not grabbed:
            break

        # Resize the frame for faster processing
        frame = cv2.resize(frame, (640, 480))

        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask for the specified color range
        lower_bound, upper_bound = color_ranges[color]
        mask = cv2.inRange(hsv, lower_bound, upper_bound)

        # Apply morphological operations to remove noise
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Check if any contours were found
        if contours:
            # Get the largest contour
            largest_contour = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)

            # Draw the bounding circle and centroid
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)

            # Print the position of the centroid
            print("Centroid Position:", (int(x), int(y)))

        # Display the frame
        cv2.imshow("Frame", frame)

        # Check for exit key
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    # Release the camera and close all windows
    camera.release()
    cv2.destroyAllWindows()

# Call the function to track objects of a specific color (e.g., "green" or "red")
track_object("green")
