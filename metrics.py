# ============================================================
# metrics.py
# Purpose: Calculate how good our model's predictions are
# We are NOT using sklearn - everything is written from scratch
# ============================================================

import numpy as np
# numpy helps us do math on entire lists of numbers at once
# instead of writing manual loops for every calculation


def mean_absolute_error(actual, predicted):
    # this function calculates MAE
    # actual = real values (numpy array)
    # predicted = our model's guesses (numpy array)

    # actual - predicted gives us the error for EVERY row at once
    # np.abs() makes every error positive (removes negative signs)
    errors = np.abs(actual - predicted)

    # np.mean() adds up all errors and divides by total count
    # this gives us the AVERAGE error
    mae = np.mean(errors)

    return mae


def mean_squared_error(actual, predicted):
    # this function calculates MSE

    # (actual - predicted) gives error for every row
    # ** 2 squares every single error (numpy applies this to all values at once)
    squared_errors = (actual - predicted) ** 2

    # average of all squared errors
    mse = np.mean(squared_errors)

    return mse


def root_mean_squared_error(actual, predicted):
    # this function calculates RMSE
    # it simply reuses our MSE function, then takes square root

    mse = mean_squared_error(actual, predicted)

    # np.sqrt() calculates the square root
    rmse = np.sqrt(mse)

    return rmse


def r2_score(actual, predicted):
    # this function calculates R2 score

    # step 1: calculate the AVERAGE of actual values
    # this represents "if we just guessed the average every time"
    mean_actual = np.mean(actual)

    # step 2: calculate total squared error of OUR model's predictions
    # this tells us how wrong OUR model was
    ss_residual = np.sum((actual - predicted) ** 2)

    # step 3: calculate total squared error IF we just guessed the average
    # this is our "baseline" comparison - the worst-case simple guess
    ss_total = np.sum((actual - mean_actual) ** 2)

    # step 4: calculate R2 using the formula we discussed
    # if our model's errors (ss_residual) are much smaller than
    # the baseline errors (ss_total), R2 will be close to 1
    r2 = 1 - (ss_residual / ss_total)

    return r2