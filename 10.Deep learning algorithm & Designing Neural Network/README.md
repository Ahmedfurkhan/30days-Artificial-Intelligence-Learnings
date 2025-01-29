# Day 10: Overview on CNN & Designing Neural Network

This repository contains the materials and resources for Day 10 of the AI Master Class series, focusing on **Convolutional Neural Networks (CNN)** and **Designing Neural Networks**. The session provides an overview of neural networks, CNN architecture, and practical implementation using Keras.

## Table of Contents
- [Day 10: Overview on CNN \& Designing Neural Network](#day-10-overview-on-cnn--designing-neural-network)
  - [Table of Contents](#table-of-contents)
  - [Neural Network Overview](#neural-network-overview)
  - [Deep Learning Algorithms](#deep-learning-algorithms)
  - [CNN Architecture](#cnn-architecture)
  - [Implementation of Neural Network](#implementation-of-neural-network)
  - [Keras Basic Syntax](#keras-basic-syntax)


## Neural Network Overview
- **Neural Network**: A network of interconnected input and output layers where each connection has an associated weight. The weights are adjusted during the learning process.
- **Perceptron**: A simple neural network with only input and output layers, used for basic decision-making.

## Deep Learning Algorithms
- **ANN (Artificial Neural Network)**: Learns any non-linear function and is known as a Universal Function Approximator. Activation functions introduce non-linearity, allowing the network to identify complex relationships between input and output.
- **RNN (Recurrent Neural Network)**: Features a looping system in the hidden layer, capturing sequential information in input data. Commonly used in NLP (Natural Language Processing) with layers like LSTM and GRU.
- **CNN (Convolutional Neural Network)**: Learns filters automatically to extract features from data, capturing spatial features (e.g., pixel arrangement). Uses convolution and pooling functions as activation functions.

## CNN Architecture
- **Convolution**: Applies a filter (kernel) to an input image to produce an output image.
- **Pooling**: Reduces the dimensionality of the input image by picking the maximum value (Max Pooling) or other operations from selected regions.

## Implementation of Neural Network
- **Backpropagation**: Calculates the error between predicted and target outputs, using gradient descent to update weights.
- **Gradient Descent**: Iteratively finds optimal values for network parameters.
- **Vanishing & Exploding Gradient**: Common issues in deep networks, addressed by techniques like gradient clipping and using LSTM networks.

## Keras Basic Syntax
- **Adding Layers**: Use `model.add(Dense(...))` to add layers to the neural network.
- **Compile Model**: Use `model.compile(...)` to define the loss function, optimizer, and metrics.
- **Batch vs Epoch**: An epoch is one pass through the entire training dataset, while a batch is a subset of samples processed before updating weights.
- **Save & Load Model**: Save the model architecture and weights using `model.to_json()` and `model.save_weights()`. Load the model using `model_from_json()` and `model.load_weights()`.

