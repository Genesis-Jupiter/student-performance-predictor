# 🎓 Student Performance Predictor

## Overview

Student Performance Predictor is a Machine Learning project that predicts a student's final grade (G3) using academic and behavioral factors such as previous grades, study time, attendance, and age.

The project includes:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Linear Regression Model
* Model Evaluation
* Cross Validation
* Streamlit Web Application

---

## Dataset

Dataset: Student Performance Dataset

Features used for prediction:

* G1 (First Period Grade)
* G2 (Second Period Grade)
* Absences
* Study Time
* Age

Target Variable:

* G3 (Final Grade)

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Matplotlib
* Git & GitHub

---

## Project Workflow

1. Load and inspect dataset
2. Handle preprocessing
3. Select important features
4. Split dataset into training and testing sets
5. Apply feature scaling
6. Train Linear Regression model
7. Evaluate performance
8. Perform cross-validation
9. Save model and scaler
10. Deploy using Streamlit

---

## Model Performance

### Linear Regression

| Metric   | Score |
| -------- | ----- |
| R² Score | ~0.86 |
| MAE      | ~0.73 |
| RMSE     | ~1.15 |

### Cross Validation

Mean R² Score:

0.79

---

## Key Insights

* Previous grades (G1 and G2) are the strongest predictors of final performance.
* Student absences have a noticeable impact on grades.
* The relationship between previous grades and final grade is largely linear.
* Linear Regression outperformed Random Forest for this dataset.

---

## Project Structure

```text
StudentPerformancePredictor/
│
├── app.py
├── train.py
├── student-por.csv
├── student_grade_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd StudentPerformancePredictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## Example Prediction

Input:

* Age = 18
* Study Time = 2
* Absences = 0
* G1 = 10
* G2 = 13

Output:

```text
Predicted Final Grade (G3): 12.8 / 20
```

---

## Future Improvements

* Add more advanced regression models
* Deploy on Streamlit Cloud
* Add visual dashboards
* Perform hyperparameter tuning
* Integrate model monitoring

---

## Author

Bhaskar Gupta

B.Tech AI & Data Engineering

Machine Learning | Data Science | AI Development
