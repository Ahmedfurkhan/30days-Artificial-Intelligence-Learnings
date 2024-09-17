import cv2

# Load the image
img = cv2.imread(r"sample2.jpg")

# Check if the image was successfully loaded
if img is None:
    print("Error: Unable to load image.")
else:
    # Convert the image to grayscale
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display the original and grayscale images
    cv2.imshow("Orig", img)
    cv2.imshow("Gray", grayImg)

    # Wait for a key press and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
