# Linear Regression Custom

## Use case
Predicts a student's final exam score (out of 100) based on study habits and academic behavior, using a Linear Regression model built completely from scratch with Gradient Descent.

## Setup
pip install -r requirements.txt
## Generate sample data (optional)
python data_generator.py
## Run the program
python main.py --data data/student_scores.csv --target final_exam_score --epochs 1000 --lr 0.01
## CSV format expected
Columns: study_hours_per_week, attendance_percentage, previous_test_score, assignments_completed, practice_questions_solved, sleep_hours_per_day, final_exam_score

## Example output metrics (local test)
MAE: 4.12

MSE: 27.85

RMSE: 5.28

R2 Score: 0.83