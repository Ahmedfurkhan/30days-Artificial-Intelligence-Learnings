import cv2
import imutils
img = cv2.imread("sample.jpeg")
resizeImg = imutils.resize(img,width=20)
cv2.imwrite("resizedImage.jpg",resizeImg)