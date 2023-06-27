import sys
sys.path.append("/opt/anaconda3/lib/python3.9/site-packages")

import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_gender=data["le_gender"]
le_sexuality=data["le_sexuality"]
le_age=data["le_age"]
le_bodyweight=data["le_bodyweight"]
le_friends=data["le_friends"]
le_fear=data["le_fear"]
le_depressed=data["le_depressed"]
le_employment=data["le_employment"]
le_education=data["le_education"]

def show_predict_page():
    st.title("Suicide Prediction")

    st.write("""### We need some information to predict the suicide""")

    gender= (
        "Female",
        "Male",
        "Transgender female",
        "Transgender male",
    )

    sexuality = (
        "Straight",
        "Bisexual",
        "Gay/Lesbian",
    )

    bodyweight={
        "Normal weight",
        "Overweight",
        "Underweight",
        "Obese",
    }

    fear={
        "Yes",
        "No",
    }

    depressed={
        "Yes",
        "No",
    }

    employment={
        "Employed for wages",
        "Out of work and looking for work",
        "Out of work but not currently looking for work",
        "A student",
        "Unable to work",
        "Retired",
        "Military",
        "Self-employed",
        "A homemaker",
    }

    education={
        "Not highly educated",
        "High school graduate",
        "Bachelor’s degree",
        "Master’s degree",
    }

    gender = st.selectbox("Gender", gender)
    sexuality = st.selectbox("Sexuality", sexuality)
    bodyweight = st.selectbox("bodyweight", bodyweight)
    employment = st.selectbox("employment", employment)
    education = st.selectbox("education", education)

    fear = st.radio("Fear", fear)
    depressed = st.radio("Depression", depressed)

    age = st.slider("Age", 0, 110, 0)
    friends = st.slider("Number of friends you have", 0, 100, 0)

    ok = st.button("Predict")
    encoder = pickle.load(open("encoders.pkl","rb"))
# [le_gender,le_sexuality,le_age,le_bodyweight,le_friends,le_fear,le_depressed,le_employment,le_education]
    if ok:
        X = np.array([[gender,sexuality,bodyweight,employment,education,fear,depressed,age,friends ]])
        X[:, 0] = le_gender.transform(X[:,0])
        X[:, 1] = le_sexuality.transform(X[:,1])
        X[:, 2] = le_bodyweight.transform(X[:,2])
        X[:, 3] = le_employment.transform(X[:,3])
        X[:, 4] = le_education.transform(X[:,4])
        X[:, 5] = le_fear.transform(X[:,5])
        X[:, 6] = le_depressed.transform(X[:,6])
        # X[:, 7] = le_age.transform(X[:,7])
        # X[:, 8] = le_friends.transform(X[:,8])
        X = X.astype(float)

        # st.write(X)
        suicide = regressor.predict(X)
        # st.write([[ 1.,  2., 22.,  2., 10.,  1.,  0.,  4.,  1.]])
        # st.write(suicide)
        msg = ""
        if not round(suicide[0]) > 0:
            msg = "The person is likely to suicide"
            st.subheader(f""+msg)
            st.subheader(f"Please contact the nearest psychiatrist")
            st.subheader(f"Emergency Toll free number: 1800-599-0019")
        else:
            msg = "The person is not likely to suicide"
            st.subheader(f""+msg)
            st.subheader(f"For more details")
            st.subheader(f"Emergency Toll free number: 1800-599-0019")