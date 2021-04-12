import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image


pickle_in = open("lr.pkl","rb")
lr=pickle.load(pickle_in)

def prediction(age, sex, bmi, children, smoker, region):

    if  sex=="Male":
        sex=1
    else:
        sex=0

    if  children=="Zero":
        children=0
    elif children=="One":
        children=1
    elif children=="Two":
        children=2
    else:
        children=3

    if  smoker=="Yes":
        smoker=1
    else:
        smoker=0

    if  region=="N":
        region=1
    elif region=="S":
        region=2
    elif region=="E":
        region=3
    else:
        region=4
        
     
    prediction1=lr.predict([[age, sex, bmi, children, smoker, region]])
    print(prediction1)
    return prediction1



def main():
    st.title("Health Insurance Price Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.slider("Age:", 0, 100)
    sex = st.selectbox('sex', options=['M','F'])
    bmi = st.number_input("bmi",20)
    children = st.selectbox('number of children', options=['Zero','One','Two','More'])
    smoker = st.selectbox('Are you an smoker?', options=['Yes','No'])
    region = st.selectbox('region', options=['N','S','E','W'])
   
    result=""
    if st.button("Predict"):
        result=prediction(age, sex, bmi, children, smoker, region)
    st.success('You would be charged around {}'.format(result))

if __name__=='__main__':
    main()