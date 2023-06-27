import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'High school graduate' in x:
        return 'High school graduate'
    return 'Not highly educated'

@st.cache_data
def load_data():
        df=pd.read_csv("suicidenew.csv")
        df=df[["gender","sexuallity","age","bodyweight","friends","social_fear","depressed","attempt_suicide","employment","edu_level"]]
        df=df.dropna()

        df['edu_level']=df['edu_level'].apply(clean_education) 
        return df

df = load_data()

def show_explore_page():
    st.title("Explore Suicide Rates")

    data = df['sexuallity'].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal") 

    st.write("""#### Suicide rates of different genders""")

    st.pyplot(fig1)

    st.write(
        """
    #### Suicide Rate Based On Gender and age
    """
    )

    data = df.groupby(["gender"])["age"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Suicide Rate Based On Gender and number of friends
    """
    )

    data = df.groupby(["gender"])["friends"].mean().sort_values(ascending=True)
    st.line_chart(data)

