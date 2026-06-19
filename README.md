<div align="center">

# Linear Regression Custom

### A Linear Regression model built completely from scratch using Gradient Descent

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-from%20scratch-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-data%20handling-150458?style=for-the-badge&logo=pandas&logoColor=white)
![No sklearn](https://img.shields.io/badge/sklearn-NOT%20USED-red?style=for-the-badge)
![Status](https://img.shields.io/badge/status-passing-brightgreen?style=for-the-badge)

</div>

---

## Use case

Predicts a student's final exam score (out of 100) from study and academic behavior features — study hours, attendance, previous test score, assignments completed, practice questions solved, and sleep hours — using a Linear Regression model trained with Gradient Descent, written entirely from scratch with no prebuilt ML libraries.

---

## What's implemented from scratch

| Component | Description |
|---|---|
| `LinearRegressionCustom` | Custom model class with `fit()` and `predict()` |
| Gradient Descent | Manual weight and bias updates over multiple epochs |
| Loss function | Mean Squared Error, calculated manually |
| Feature scaling | Manual standardization (mean / standard deviation) |
| Train/test split | Custom 80/20 split using manual shuffling and indexing |
| Metrics | MAE, MSE, RMSE, and R2 score, all coded manually |

No `sklearn.linear_model`, no `sklearn` preprocessing, and no prebuilt train/test split were used anywhere in this project.

---

## Project structure

```
Linear-Regression-Custom/
README.md
requirements.txt
main.py
linear_regression.py
preprocessing.py
metrics.py
data_generator.py
data/
    student_scores.csv
outputs/
    predictions.csv
.gitignore
```

---

## Setup

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Generate sample data (optional)

A sample dataset generator is included for local testing:

```bash
python data_generator.py
```

This creates `data/student_scores.csv` with 300 rows of realistic, randomly generated student data.

## Run the program

```bash
python main.py --data data/student_scores.csv --target final_exam_score --epochs 1000 --lr 0.01
```

| Argument | Description | Default |
|---|---|---|
| `--data` | Path to the input CSV file | required |
| `--target` | Name of the target column to predict | required |
| `--epochs` | Number of gradient descent training iterations | 1000 |
| `--lr` | Learning rate for gradient descent | 0.01 |

---

## CSV format expected

| Column | Type / range |
|---|---|
| `study_hours_per_week` | numeric, 0 to 50 |
| `attendance_percentage` | numeric, 0 to 100 |
| `previous_test_score` | numeric, 0 to 100 |
| `assignments_completed` | numeric, 0 to 20 |
| `practice_questions_solved` | numeric, 0 to 500 |
| `sleep_hours_per_day` | numeric, 0 to 12 |
| `final_exam_score` | numeric, 0 to 100 (target) |

The program works with any CSV that follows this column structure — it is not tied to one fixed dataset.

---

## Example output (local test run)

```
Loaded 300 rows and 7 columns
Input features: ['study_hours_per_week', 'attendance_percentage', 'previous_test_score',
                  'assignments_completed', 'practice_questions_solved', 'sleep_hours_per_day']
Target column: final_exam_score
Training rows: 240
Testing rows: 60
Final learned weights: [10.81308317  3.96242656  6.21331851  5.83877093  4.63021615  0.43329791]
Final learned bias: 80.44095134586557

MAE: 4.3760
MSE: 29.6679
RMSE: 5.4468
R2 Score: 0.7922

Predictions saved to outputs/predictions.csv
```

| Metric | Result | Required minimum |
|---|---|---|
| R2 Score | 0.7922 | >= 0.75 |
| MAE | 4.3760 | <= 8.0 |

---

<div align="center">

Built as part of a Machine Learning assignment — custom Linear Regression implementation, no shortcuts.

</div>
