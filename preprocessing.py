# ============================================================
# preprocessing.py
# Purpose: 
#   1. Scale features manually (standardization)
#   2. Split data into training and testing sets manually
# We are NOT using sklearn for either of these - written from scratch
# ============================================================

import numpy as np
# numpy helps with array math (mean, standard deviation, shuffling)


def standardize_features(X):
    # this function scales our features so they are on a similar range
    # X = our feature matrix (a 2D table of numbers - rows = students, columns = features)

    # calculate the MEAN of each column
    # axis=0 means "calculate down each column" (not across rows)
    mean = np.mean(X, axis=0)

    # calculate the STANDARD DEVIATION of each column
    std = np.std(X, axis=0)

    # apply the formula: (value - mean) / standard_deviation
    # numpy automatically applies this to EVERY value in EVERY column at once
    X_scaled = (X - mean) / std

    # we return the scaled data AND the mean/std values
    # WHY return mean and std too? because later, when we get NEW data
    # (like a hidden test CSV), we must scale it using the SAME mean/std
    # that we learned from our TRAINING data - not recalculate new ones
    return X_scaled, mean, std


def apply_standardization(X, mean, std):
    # this function applies EXISTING mean/std to NEW data
    # used for test data or future predictions
    # we do NOT recalculate mean/std here - we reuse the ones from training

    X_scaled = (X - mean) / std
    return X_scaled


def train_test_split_custom(X, y, test_size=0.2, random_seed=42):
    # this function splits our data into training and testing sets
    # X = features, y = target column (final_exam_score)
    # test_size=0.2 means 20% of data goes to testing
    # random_seed ensures we get the SAME random split every time we run this
    # (makes our results reproducible - same as random_state in sklearn)

    # np.random.seed() locks in the randomness so it's repeatable
    np.random.seed(random_seed)

    # total number of rows in our dataset
    total_rows = X.shape[0]
    # X.shape gives us (number_of_rows, number_of_columns)
    # [0] grabs just the number of rows

    # create a list of indices [0, 1, 2, 3, ... total_rows-1]
    # these represent the "row numbers" of our data
    indices = np.arange(total_rows)

    # shuffle these indices randomly
    # this is like shuffling a deck of cards before splitting it
    np.random.shuffle(indices)

    # calculate how many rows should go into the TEST set
    # e.g., if total_rows = 300 and test_size = 0.2, test_count = 60
    test_count = int(total_rows * test_size)

    # split the SHUFFLED indices into two groups
    test_indices = indices[:test_count]        # first 20% of shuffled indices
    train_indices = indices[test_count:]       # remaining 80% of shuffled indices

    # use these indices to actually pull out the corresponding rows
    # from X and y
    X_train = X[train_indices]
    X_test = X[test_indices]
    y_train = y[train_indices]
    y_test = y[test_indices]

    return X_train, X_test, y_train, y_test