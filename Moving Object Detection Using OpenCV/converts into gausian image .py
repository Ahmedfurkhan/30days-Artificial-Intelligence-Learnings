import cv2
img = cv2.imread("sample.jpeg")
gaussianBlurImg = cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("gaussianImage.jpg",gaussianBlurImg)
