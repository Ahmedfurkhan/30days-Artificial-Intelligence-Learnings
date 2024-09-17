import cv2
import os

# Get the current directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Provide the full path to the cascade file
cascade_path = os.path.join(script_dir, 'haarcascade_frontalface_default.xml')

# Check if the cascade file exists
if not os.path.isfile(cascade_path):
    print("Error: Cascade file not found!")
    exit()

# Load the cascade classifier
face_cascade = cv2.CascadeClassifier(cascade_path)

datasets = 'dataset'  
sub_data = 'champ'     

# Create the 'dataset' directory if it doesn't exist
if not os.path.isdir(datasets):
    os.mkdir(datasets)

path = os.path.join(datasets, sub_data)

# Create the 'champ' directory if it doesn't exist
if not os.path.isdir(path):
    os.mkdir(path)

(width, height) = (130, 100)
webcam = cv2.VideoCapture(0)

count = 1
while count < 31:
    print(count)
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.png' % (path, count), face_resize)
    count += 1
    
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break
print("Dataset obtained successfully")
webcam.release()
cv2.destroyAllWindows()
