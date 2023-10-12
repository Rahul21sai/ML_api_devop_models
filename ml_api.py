# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

class model_input(BaseModel):
    
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction :float
    Age :int
    
    
#loading the save model
diabetes_model = pickle.load(open('diabetes_model (1).sav','rb'))

@app.post('/diabetes_prediction')

def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dicitionary = json.loads(input_data)
    
    preg = input_dicitionary['Pregnancies']
    glu = input_dicitionary['Glucose']
    bp = input_dicitionary['BloodPressure']
    skin = input_dicitionary['SkinThickness']
    insulin = input_dicitionary['Insulin']
    bmi = input_dicitionary['BMI']
    dpf = input_dicitionary['DiabetesPedigreeFunction']
    age = input_dicitionary['Age']
    
    
    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'the person is not Diabetic'
    else:
        return 'the person is Diabetic'