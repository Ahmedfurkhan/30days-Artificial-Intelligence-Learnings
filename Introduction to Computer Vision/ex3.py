import cv2

# Load the image
img = cv2.imread(r"sample1.jpg")

# Check if the image was successfully loaded
if img is None:
    print("Error: Unable to load image.")
else:
    # Convert the image to grayscale
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite("GrayImage.jpg", grayImg)

    # Display the original and grayscale images
    cv2.imshow("Original", img)
    cv2.imshow("GrayImage", grayImg)

    # Wait for a key press and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
