from numpy import loadtxt
from keras.models import model_from_json
import os

# Check if files exist
for file in ["model.json", "model.weights.h5", "pima-indians-diabetes.csv"]:
    if not os.path.exists(file):
        raise FileNotFoundError(f"Error: '{file}' not found in the current directory.")

# Load dataset
dataset = loadtxt("pima-indians-diabetes.csv", delimiter=',')
x = dataset[:, 0:8]
y = dataset[:, 8]

# Load model from JSON
with open("model.json", 'r') as json_file:
    loaded_model_json = json_file.read()

model = model_from_json(loaded_model_json)
model.load_weights("model.weights.h5")
print("Loaded model from disk")

# Predict
predictions = (model.predict(x) > 0.5).astype("int32")

# Print some predictions
for i in range(5, 10):
    print('%s => %d (expected %d)' % (x[i].tolist(), predictions[i][0], y[i]))
