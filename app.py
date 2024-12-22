#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI
import joblib
import pandas as pd

# Load the saved model
model = joblib.load("credit_score_model.pkl")

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Credit Score Prediction API is running!"}

@app.post("/predict/")
def predict(data: dict):
    try:
        # Convert input data into a DataFrame
        input_data = pd.DataFrame([data])
        
        # Make predictions
        prediction = model.predict(input_data)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        return {"error": str(e)}


# In[ ]:




