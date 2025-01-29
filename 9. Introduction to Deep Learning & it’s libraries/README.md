Day 9: Introduction to Deep Learning & its Libraries

This repository contains the materials and resources for Day 9 of the AI Master Class series, focusing on **Deep Learning** and its libraries. The session provides an overview of deep learning concepts, activation functions, and popular deep learning libraries like TensorFlow, Keras, and PyTorch.

## Table of Contents
- [AI Master Class - Day 9: Introduction to Deep Learning \& its Libraries](#ai-master-class---day-9-introduction-to-deep-learning--its-libraries)
  - [Table of Contents](#table-of-contents)
  - [Overview on Deep Learning](#overview-on-deep-learning)
  - [Neurons \& Activation Functions](#neurons--activation-functions)
  - [Deep Learning Libraries](#deep-learning-libraries)
  - [Applications of Deep Learning](#applications-of-deep-learning)
  - [Installation Instructions](#installation-instructions)
- [Install TensorFlow](#install-tensorflow)
- [Install Keras](#install-keras)
- [Install Pandas](#install-pandas)
- [Install Scipy](#install-scipy)
- [Install PyTorch](#install-pytorch)

## Overview on Deep Learning
- **What is Deep Learning?**: Deep Learning is a subset of machine learning that uses neural networks with multiple layers to model complex patterns in data.
- **Why Deep Learning?**: Deep Learning excels at automatic feature extraction and is particularly useful for tasks like image recognition, speech recognition, and natural language processing.
- **CPU vs GPU**: GPUs are preferred for deep learning tasks due to their ability to process large amounts of data in parallel, making them faster and more efficient for training deep learning models.

## Neurons & Activation Functions
- **Neurons**: Inspired by the human brain, a neuron in a neural network takes inputs, applies a mathematical function (activation function), and produces an output.
- **Activation Functions**:
  - **Step Function**: Outputs 1 if the input is greater than or equal to 0, otherwise 0.
  - **Sigmoid Function**: Outputs values between 0 and 1, useful for capturing non-linearity.
  - **Tanh Function**: A rescaled version of the sigmoid function with outputs between -1 and 1.
  - **ReLU Function**: Returns 0 for negative inputs and the input value for positive inputs.
  - **Leaky ReLU**: Similar to ReLU but allows a small, non-zero gradient for negative inputs.
  - **Softmax Function**: Used in the final layer of a neural network to convert outputs into a probability distribution.

## Deep Learning Libraries
- **TensorFlow**: A powerful open-source library for numerical computation and large-scale machine learning.
- **Keras**: A high-level neural networks API, written in Python and capable of running on top of TensorFlow.
- **PyTorch**: An open-source machine learning library developed by Facebook, widely used for research and production.
- **Pandas**: A library for data manipulation and analysis.
- **Scipy**: A library for scientific and technical computing.

## Applications of Deep Learning
- **Fruit & Vegetable Classification**: Using deep learning to classify different types of fruits and vegetables.
- **AI in Cooking**: Automating cooking processes using AI.
- **AI in Autonomous Vehicles**: Enabling self-driving cars to recognize and navigate their environment.
- **AI Doctor**: Predicting diseases from medical images.
- **Voice Recognition for ALS Patients**: Assisting patients with ALS through voice recognition technology.

## Installation Instructions
To install the necessary libraries, run the following commands:

```bash
# Install TensorFlow
pip install tensorflow

# Install Keras
pip install keras

# Install Pandas
pip install pandas

# Install Scipy
pip install scipy==1.1.0

# Install PyTorch
pip3 install --find-links https://download.pytorch.org/whl/torch_stable.html torch==1.3.1 torchvision==0.4.2