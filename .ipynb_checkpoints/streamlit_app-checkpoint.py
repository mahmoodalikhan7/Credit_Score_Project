import streamlit as st
import requests

# URL of your deployed FastAPI model on Heroku (replace with your actual URL)
API_URL = "https://creditscore-fastapi-78b7496457f0.herokuapp.com/predict"

# Streamlit app title
st.title('Credit Score Classification')

# Input form for user data
st.subheader("Enter the details to predict credit score:")

# Input fields for user data
monthly_salary = st.number_input("Monthly Inhand Salary", min_value=1000.0, step=100.0)
num_bank_accounts = st.number_input("Number of Bank Accounts", min_value=0, step=1)
num_credit_card = st.number_input("Number of Credit Cards", min_value=0, step=1)
interest_rate = st.number_input("Interest Rate", min_value=0.0, step=0.1)
occupation = st.selectbox("Occupation", ['Salaried', 'Self-Employed', 'Others'])
credit_mix = st.selectbox("Credit Mix", ['Good', 'Bad'])
credit_history_age = st.number_input("Credit History Age (in years)", min_value=0.0, step=0.1)

# When the button is clicked, send a request to the FastAPI model
if st.button("Predict"):
    # Prepare data for API request
    input_data = {
        "Monthly_Inhand_Salary": monthly_salary,
        "Num_Bank_Accounts": num_bank_accounts,
        "Num_Credit_Card": num_credit_card,
        "Interest_Rate": interest_rate,
        "Occupation": occupation,
        "Credit_Mix": credit_mix,
        "Credit_History_Age": credit_history_age
    }

    # Send the input data to FastAPI for prediction
    try:
        response = requests.post(API_URL, json=input_data)

        # Check if the request was successful
        if response.status_code == 200:
            prediction = response.json()['prediction']
            st.success(f"The predicted credit score classification is: {prediction}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while contacting the API: {e}")
