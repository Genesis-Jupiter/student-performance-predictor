import streamlit as st
import pandas as pd
import pickle

# ==========================
# Load Model & Scaler
# ==========================

model = pickle.load(open("student_grade_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# ==========================
# Title
# ==========================

st.title("🎓 Student Performance Predictor")

st.write(
    """
    Predict a student's final grade (G3) based on:
    - Previous Grades
    - Study Time
    - Absences
    - Age
    """
)

st.divider()

# ==========================
# Input Section
# ==========================

st.subheader("Enter Student Details")

age = st.number_input(
    "Age",
    min_value=15,
    max_value=25,
    value=18
)

studytime = st.selectbox(
    "Study Time",
    options=[1, 2, 3, 4],
    help="""
    1 = < 2 hours/week
    2 = 2–5 hours/week
    3 = 5–10 hours/week
    4 = > 10 hours/week
    """
)

absences = st.number_input(
    "Number of Absences",
    min_value=0,
    max_value=100,
    value=0
)

G1 = st.number_input(
    "First Period Grade (G1)",
    min_value=0,
    max_value=20,
    value=10
)

G2 = st.number_input(
    "Second Period Grade (G2)",
    min_value=0,
    max_value=20,
    value=10
)

# ==========================
# Prediction
# ==========================

if st.button("Predict Final Grade"):

    input_data = pd.DataFrame({
        "G1": [G1],
        "G2": [G2],
        "absences": [absences],
        "studytime": [studytime],
        "age": [age]
    })

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]

    # Keep prediction within valid grade range
    prediction = max(0, min(20, prediction))

    st.divider()

    st.subheader("📊 Prediction Result")

    st.success(
        f"Predicted Final Grade (G3): {prediction:.2f} / 20"
    )

    # Performance Category

    if prediction >= 16:
        st.balloons()
        st.success("🌟 Excellent Performance")

    elif prediction >= 12:
        st.info("👍 Good Performance")

    elif prediction >= 10:
        st.warning("📚 Average Performance")

    else:
        st.error("⚠️ Needs Improvement")

# ==========================
# Footer
# ==========================

st.divider()

st.caption(
    "Built with Scikit-Learn, Pandas and Streamlit"
)