# ============================================================
# data_generator.py
# Purpose: Create a sample CSV file with realistic student data
# for testing our Linear Regression model
# ============================================================

import numpy as np
import pandas as pd


def generate_student_data(num_rows=300, save_path="data/student_scores.csv"):
    # num_rows = how many student records to generate
    # save_path = where to save the CSV file

    # lock randomness so we get the SAME data every time we run this
    np.random.seed(42)

    # generate random values for each feature within their allowed ranges
    study_hours_per_week = np.random.uniform(0, 50, num_rows)
    attendance_percentage = np.random.uniform(40, 100, num_rows)
    previous_test_score = np.random.uniform(20, 100, num_rows)
    assignments_completed = np.random.uniform(0, 20, num_rows)
    practice_questions_solved = np.random.uniform(0, 500, num_rows)
    sleep_hours_per_day = np.random.uniform(4, 12, num_rows)

    # create the target column (final_exam_score) using a realistic formula
    # plus some random noise, so it's not a PERFECT straight-line relationship
    # NOTE: this formula is ONLY used to generate fake practice data
    # the model itself will NEVER see this formula - it must learn the pattern itself
    noise = np.random.normal(0, 5, num_rows)

    final_exam_score = (
        (study_hours_per_week * 0.8) +
        (attendance_percentage * 0.25) +
        (previous_test_score * 0.3) +
        (assignments_completed * 1.2) +
        (practice_questions_solved * 0.04) +
        (sleep_hours_per_day * 0.5) +
        noise
    )

    # clip final scores so they stay within 0 to 100
    final_exam_score = np.clip(final_exam_score, 0, 100)

    # put everything into a pandas DataFrame (table format)
    data = pd.DataFrame({
        "study_hours_per_week": study_hours_per_week,
        "attendance_percentage": attendance_percentage,
        "previous_test_score": previous_test_score,
        "assignments_completed": assignments_completed,
        "practice_questions_solved": practice_questions_solved,
        "sleep_hours_per_day": sleep_hours_per_day,
        "final_exam_score": final_exam_score
    })

    # save this table as a CSV file
    data.to_csv(save_path, index=False)
    # index=False means we don't save an extra "row number" column

    print(f"Generated {num_rows} rows of data and saved to {save_path}")


# this block only runs if we execute this file directly
# (not if it's imported into another file)
if __name__ == "__main__":
    generate_student_data()