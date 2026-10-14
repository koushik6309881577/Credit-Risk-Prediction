
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="CreditWise | Credit Risk Prediction",
    page_icon="💳",
    layout="wide"
)

@st.cache_resource
def load_models():
    return joblib.load("credit_models.joblib")

@st.cache_data
def load_results():
    return pd.read_csv("model_results.csv")

models = load_models()
results = load_results()

st.title("💳 CreditWise")
st.subheader("Credit Risk Prediction Using Machine Learning")
st.write(
    "Explore estimated loan-default risk using financial information "
    "and trained machine learning models."
)

st.info(
    "Educational project only. Predictions are estimates, not "
    "official credit scores or lending decisions."
)

st.header("Enter Financial Details")

with st.form("credit_form"):
    col1, col2 = st.columns(2)

    with col1:
        person_age = st.number_input(
            "Age", min_value=18, max_value=100, value=25
        )
        person_income = st.number_input(
            "Annual income", min_value=0, value=50000, step=1000
        )
        person_home_ownership = st.selectbox(
            "Home ownership", ["RENT", "OWN", "MORTGAGE", "OTHER"]
        )
        person_emp_length = st.number_input(
            "Employment length (years)", min_value=0.0,
            max_value=60.0, value=3.0, step=0.5
        )
        loan_intent = st.selectbox(
            "Loan purpose",
            ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE",
             "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"]
        )

    with col2:
        loan_grade = st.selectbox(
            "Loan grade", ["A", "B", "C", "D", "E", "F", "G"]
        )
        loan_amnt = st.number_input(
            "Loan amount", min_value=1, value=10000, step=500
        )
        loan_int_rate = st.number_input(
            "Interest rate (%)", min_value=0.0,
            max_value=100.0, value=10.0, step=0.5
        )
        cb_person_default_on_file = st.selectbox(
            "Previous default recorded", ["N", "Y"]
        )
        cb_person_cred_hist_length = st.number_input(
            "Credit history length (years)", min_value=0,
            max_value=80, value=3
        )

    loan_percent_income = (
        loan_amnt / person_income if person_income > 0 else 0.0
    )

    selected_model = st.selectbox(
        "Choose prediction model", list(models.keys())
    )

    submitted = st.form_submit_button(
        "Predict Credit Risk", type="primary"
    )

if submitted:
    input_data = pd.DataFrame([{
        "person_age": person_age,
        "person_income": person_income,
        "person_home_ownership": person_home_ownership,
        "person_emp_length": person_emp_length,
        "loan_intent": loan_intent,
        "loan_grade": loan_grade,
        "loan_amnt": loan_amnt,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_default_on_file": cb_person_default_on_file,
        "cb_person_cred_hist_length": cb_person_cred_hist_length
    }])

    feature_columns = joblib.load("feature_columns.joblib")
    input_data = input_data[feature_columns]

    model = models[selected_model]
    prediction = int(model.predict(input_data)[0])
    probability = float(model.predict_proba(input_data)[0][1])

    st.header("Prediction Result")

    if prediction == 1:
        st.warning("The model predicts a higher risk of loan default.")
    else:
        st.success("The model predicts a lower risk of loan default.")

    st.metric("Estimated default probability", f"{probability:.1%}")
    st.caption(
        "This probability is model-dependent and may not be calibrated. "
        "It is not a guarantee of future repayment."
    )

st.divider()
st.header("Model Performance Comparison")
st.dataframe(results,width=True, hide_index=True)

st.caption(
    "Performance is measured on a held-out test set. "
    "Results depend on the dataset and train/test split."
)
