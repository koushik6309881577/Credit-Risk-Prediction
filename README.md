# CreditWise – Credit Risk Prediction

## 📌 Project Overview

**CreditWise** is a Machine Learning-based Credit Risk Prediction web application developed using Python and Streamlit. It predicts the likelihood of a borrower defaulting on a loan based on their financial details, employment information, loan characteristics, and credit history.

The project demonstrates how machine learning classification algorithms can be applied to credit risk analysis through an interactive and user-friendly web interface.

🌐 **Live Application:** https://creditcard-risk-predictions.streamlit.app/

## 🎯 Objectives

- Predict potential loan default risk using machine learning.
- Compare the performance of multiple classification algorithms.
- Provide an interactive interface for entering borrower and loan information.
- Display prediction results and estimated default probabilities.
- Demonstrate an end-to-end machine learning workflow, from data preprocessing to web application deployment.

## ✨ Features

- **Interactive Web Interface:** Enter borrower details and loan information through a Streamlit application.
- **Multiple ML Models:** Includes Logistic Regression, Decision Tree, and Random Forest classifiers.
- **Risk Prediction:** Predicts whether a loan application falls into the model's default or non-default class.
- **Probability Display:** Displays the model-estimated probability associated with the default class.
- **Model Comparison:** Presents model performance results for comparison.
- **Automated Feature Calculation:** Calculates the loan-to-income ratio from the loan amount and annual income.
- **Data Preprocessing:** Handles missing values and transforms numerical and categorical features.
- **Online Deployment:** Accessible through a public Streamlit Community Cloud link.

## 🧠 Machine Learning Algorithms

### 1. Logistic Regression
A classification algorithm that estimates the probability of a borrower belonging to a particular class. It provides a useful baseline for binary classification.

### 2. Decision Tree Classifier
A tree-based algorithm that makes predictions by following decision rules learned from the training data.

### 3. Random Forest Classifier
An ensemble learning algorithm that combines predictions from multiple decision trees to improve predictive performance and generalization.

## 📊 Dataset

The project uses the **Credit Risk Dataset** available on Kaggle.

**Dataset:** https://www.kaggle.com/datasets/laotse/credit-risk-dataset

The dataset contains borrower information, loan details, and historical credit indicators.

The target variable is `loan_status`:

- `0` – No recorded loan default in the dataset.
- `1` – Loan default recorded in the dataset.

### Features Used

| Feature | Description |
|---|---|
| `person_age` | Borrower's age |
| `person_income` | Borrower's annual income |
| `person_home_ownership` | Home ownership status |
| `person_emp_length` | Employment length in years |
| `loan_intent` | Purpose of the loan |
| `loan_grade` | Assigned loan grade |
| `loan_amnt` | Requested loan amount |
| `loan_int_rate` | Loan interest rate |
| `loan_percent_income` | Loan amount as a proportion of income |
| `cb_person_default_on_file` | Historical default indicator |
| `cb_person_cred_hist_length` | Length of credit history |

## ⚙️ Project Workflow

1. **Data Collection:** Load the credit risk dataset.
2. **Data Preprocessing:** Handle missing values and prepare numerical and categorical features.
3. **Feature Transformation:** Scale numerical features and encode categorical variables.
4. **Data Splitting:** Divide the dataset into training and testing sets using stratified sampling.
5. **Model Training:** Train Logistic Regression, Decision Tree, and Random Forest classifiers.
6. **Model Evaluation:** Compare model performance using accuracy, precision, recall, F1-score, and ROC-AUC.
7. **Model Saving:** Save the trained models and feature information using Joblib.
8. **Application Development:** Build an interactive interface using Streamlit.
9. **Deployment:** Deploy the application using Streamlit Community Cloud.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Model Persistence:** Joblib
- **Web Framework:** Streamlit
- **Development Environment:** Google Colab and Visual Studio Code
- **Dataset Source:** Kaggle
- **Deployment Platform:** Streamlit Community Cloud
- **Version Control:** Git and GitHub

## 📁 Project Structure

```text
credit-risk-prediction/
│
├── app.py
├── requirements.txt
├── credit_models.joblib
├── feature_columns.joblib
├── model_results.csv
└── README.md
```

### File Descriptions

- `app.py` – Contains the Streamlit application and prediction interface.
- `requirements.txt` – Lists the Python dependencies required to run the application.
- `credit_models.joblib` – Stores the trained machine learning models.
- `feature_columns.joblib` – Stores the feature information used by the models.
- `model_results.csv` – Contains the saved model evaluation results.
- `README.md` – Documents the project, technologies, workflow, and usage instructions.

## 🚀 Run the Project Locally

### Prerequisites

Install Python and Git, then clone the repository.

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/credit-risk-prediction.git
```

Replace `YOUR-GITHUB-USERNAME` with your GitHub username.

### Step 2: Navigate to the Project Folder

```bash
cd credit-risk-prediction
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at:

`http://localhost:8501`

## 🌐 Live Demo

Try the deployed application here:

**https://creditcard-risk-predictions.streamlit.app/**

Enter the requested borrower and loan details to view the model's prediction and estimated default probability.

## 📈 Model Evaluation

The models are evaluated using the following metrics:

- **Accuracy:** Measures the proportion of correct predictions.
- **Precision:** Measures how many predicted defaults were actual defaults.
- **Recall:** Measures how many actual defaults the model identified.
- **F1-score:** Balances precision and recall.
- **ROC-AUC:** Measures how well the model distinguishes between the two classes across classification thresholds.

The project includes a model comparison table to help assess the strengths and weaknesses of the selected algorithms. Refer to `model_results.csv` for the actual evaluation results.

## 🔮 Future Enhancements

- Add visualizations for loan characteristics and risk patterns.
- Improve model tuning and compare additional classification algorithms.
- Add explainability tools to show which features influence predictions.
- Enhance the interface with more interactive charts.
- Add input validation and clearer explanations of prediction results.
- Evaluate fairness and model performance across different borrower groups.

## ⚠️ Disclaimer

CreditWise is an educational machine learning project intended for demonstration and learning purposes. Its predictions are based on patterns in the training dataset and should not be used as the sole basis for actual lending, credit approval, or financial decisions. Model predictions are estimates and are not guarantees of future borrower behavior.

## 👨‍💻 Author

Developed as a machine learning project to explore credit risk prediction, classification algorithms, and deployment of an interactive web application.

## 📄 License

This project is available for educational and learning purposes. Add a specific open-source license if you intend to permit reuse under defined terms.
