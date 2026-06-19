# ============================================================
# linear_regression.py
# Purpose: Custom Linear Regression model built from scratch
# Uses Gradient Descent to learn weights and bias
# ============================================================

import numpy as np


class LinearRegressionCustom:

    def __init__(self, learning_rate=0.01, epochs=1000):
        # learning_rate controls how big each gradient descent step is
        self.learning_rate = learning_rate

        # epochs = how many times we repeat the training loop
        self.epochs = epochs

        # weights will hold one number per feature (learned during training)
        self.weights = None

        # bias is the intercept term (like 'c' in y = mx + c)
        self.bias = None

        # loss_history stores the loss at each epoch, so we can see it decreasing
        self.loss_history = []

    def fit(self, X, y):
        # X = training features (2D array: rows = samples, columns = features)
        # y = training target values (1D array: actual final_exam_score values)

        n_samples, n_features = X.shape
        # n_samples = number of rows (students)
        # n_features = number of columns (study_hours, attendance, etc.)

        # initialize weights as zeros, one per feature
        self.weights = np.zeros(n_features)

        # initialize bias as zero
        self.bias = 0

        # gradient descent loop - repeat 'epochs' times
        for epoch in range(self.epochs):

            # step 1: calculate current predictions using current weights and bias
            # this is y = X.w + b, done for all rows at once using matrix multiplication
            y_predicted = np.dot(X, self.weights) + self.bias

            # step 2: calculate the error for every row
            error = y_predicted - y

            # step 3: calculate gradients (direction to adjust weights and bias)
            # gradient for weights: average of (error * corresponding feature value)
            dw = (1 / n_samples) * np.dot(X.T, error)
            # X.T means "transpose" - flips rows and columns so the math lines up correctly

            # gradient for bias: average of all errors
            db = (1 / n_samples) * np.sum(error)

            # step 4: update weights and bias by moving AGAINST the gradient
            # this reduces the error (moving downhill toward the lowest cost)
            self.weights = self.weights - self.learning_rate * dw
            self.bias = self.bias - self.learning_rate * db

            # step 5: calculate and store the current loss (Mean Squared Error)
            # this lets us see if loss is decreasing over time
            loss = np.mean(error ** 2)
            self.loss_history.append(loss)

    def predict(self, X):
        # uses the learned weights and bias to make predictions on new data
        # same formula as during training: y = X.w + b
        return np.dot(X, self.weights) + self.bias