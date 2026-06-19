# ============================================================
# main.py
# Purpose: Ties everything together
# Loads data, preprocesses it, trains the model, evaluates it,
# and saves predictions
# Run from terminal with arguments, e.g.:
# python main.py --data data/student_scores.csv --target final_exam_score --epochs 1000 --lr 0.01
# ============================================================

import argparse
import numpy as np
import pandas as pd
import os

from linear_regression import LinearRegressionCustom
from preprocessing import standardize_features, apply_standardization, train_test_split_custom
from metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score


def main():
    # ---- step 1: set up command line arguments ----
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True, help="Path to CSV file")
    parser.add_argument("--target", type=str, required=True, help="Name of target column")
    parser.add_argument("--epochs", type=int, default=1000, help="Number of training epochs")
    parser.add_argument("--lr", type=float, default=0.01, help="Learning rate")
    args = parser.parse_args()
    # this lets us run: python main.py --data data/student_scores.csv --target final_exam_score --epochs 1000 --lr 0.01

    # ---- step 2: load the CSV file ----
    df = pd.read_csv(args.data)

    print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns")

    # ---- step 3: handle missing values ----
    # strategy: fill any missing numeric values with the column's mean
    df = df.fillna(df.mean(numeric_only=True))

    # ---- step 4: separate features (X) and target (y) ----
    feature_columns = [col for col in df.columns if col != args.target]
    print(f"Input features: {feature_columns}")
    print(f"Target column: {args.target}")

    X = df[feature_columns].values
    # .values converts the pandas table into a plain numpy array

    y = df[args.target].values

    # ---- step 5: split into train and test sets (custom function) ----
    X_train, X_test, y_train, y_test = train_test_split_custom(X, y, test_size=0.2, random_seed=42)

    print(f"Training rows: {X_train.shape[0]}")
    print(f"Testing rows: {X_test.shape[0]}")

    # ---- step 6: scale features (standardization, fit on training data only) ----
    X_train_scaled, mean, std = standardize_features(X_train)

    # apply the SAME mean/std to test data (do not recalculate on test data)
    X_test_scaled = apply_standardization(X_test, mean, std)

    # ---- step 7: train the model ----
    model = LinearRegressionCustom(learning_rate=args.lr, epochs=args.epochs)
    model.fit(X_train_scaled, y_train)

    print(f"Final learned weights: {model.weights}")
    print(f"Final learned bias: {model.bias}")

    # ---- step 8: make predictions on test data ----
    predictions = model.predict(X_test_scaled)

    # ---- step 9: calculate metrics ----
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = root_mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print(f"MAE: {mae:.4f}")
    print(f"MSE: {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R2 Score: {r2:.4f}")

    # ---- step 10: save predictions to outputs/predictions.csv ----
    os.makedirs("outputs", exist_ok=True)
    # exist_ok=True means don't throw an error if the folder already exists

    results = pd.DataFrame({
        "actual": y_test,
        "predicted": predictions
    })

    output_path = "outputs/predictions.csv"
    results.to_csv(output_path, index=False)

    print(f"Predictions saved to {output_path}")


if __name__ == "__main__":
    main()