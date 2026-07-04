# 🧠 Linear Regression Custom

> **Predicts a student's final exam score (out of 100) based on study habits and academic behavior — built completely from scratch using Gradient Descent. No sklearn. No shortcuts.**

---

## 💡 Use Case

Models the relationship between a student's **study habits** and **academic behavior** to predict their **final exam score**, using a Linear Regression engine powered by a custom Gradient Descent optimizer — written entirely from scratch in Python.

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
```

---

## 📊 Generate Sample Data *(optional)*

```bash
python data_generator.py
```

---

## 🚀 Run the Model

```bash
python main.py \
  --data data/student_scores.csv \
  --target final_exam_score \
  --epochs 1000 \
  --lr 0.01
```

---

## 📁 CSV Format

Expected columns in your dataset:

| Column | Description |
|--------|-------------|
| `study_hours_per_week` | Weekly study hours |
| `attendance_percentage` | Class attendance % |
| `previous_test_score` | Score from last test |
| `assignments_completed` | No. of assignments done |
| `practice_questions_solved` | Practice questions solved |
| `sleep_hours_per_day` | Average sleep per day |
| `final_exam_score` | ✅ **Target column** (0–100) |

---

## 📈 Model Performance *(local test)*

| Metric | Value | Meaning |
|--------|-------|---------|
| **MAE** | `4.12` | Mean Absolute Error |
| **MSE** | `27.85` | Mean Squared Error |
| **RMSE** | `5.28` | Root Mean Squared Error |
| **R² Score** | `0.83` | 83% variance explained |

---

## 🔧 How It Works

1. **Data Loading** — reads CSV, separates features and target
2. **Preprocessing** — normalizes input features
3. **Gradient Descent** — iteratively minimizes MSE loss
4. **Prediction** — outputs final exam score per student
5. **Evaluation** — computes MAE, MSE, RMSE, R²

---

## 🗂️ Project Structure

```
├── main.py               # Entry point
├── data_generator.py     # Sample data generator
├── data/
│   └── student_scores.csv
├── requirements.txt
└── README.md
```

---

## 📦 Requirements

```
numpy
pandas
matplotlib
```

---

*Built with ❤️ — Pure Python · No ML libraries · Custom Gradient Descent*
