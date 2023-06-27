import sys
sys.path.append("/opt/anaconda3/lib/python3.9/site-packages")

import streamlit as st
from PIL import Image

def show_reference_page():
    page = st.sidebar.selectbox("Select", ("Videos", "Blogs"))

    if page == "Videos":
        image = Image.open("hope.png")
        st.image(image, width=300)

        st.header("Videos")
        link = """
        <head>
        </head>
        <body>
        <a href="https://www.youtube.com/watch?v=Qq-xrQKx1Pg&t=4s">Suicide and Self-Harm</a> <br>
        <a href="https://www.youtube.com/watch?v=d6rTv8nSAhM">Why do people self-harm?</a> <br>
        <a href="https://www.youtube.com/watch?v=i7eE5G5Baps">Suicide Prevention: You are not alone</a> <br>
        <a href="https://www.youtube.com/watch?v=3BByqa7bhto">Teen Suicide Prevention</a> <br>
        <a href="https://www.youtube.com/watch?v=CuimBMUP5fc">Suicide Awareness and Prevention</a> <br>
        <a href="https://www.youtube.com/watch?v=TokWrCfq_Cc">Youth Suicide Prevention</a> <br>
        <a href="https://www.youtube.com/watch?v=lHBppEHBu2Y">Care Like Family</a> <br>
        </body>
        """
        st.markdown(link, unsafe_allow_html = True)    

    else:
        image = Image.open("alone.jpg")
        st.image(image, width=700)

        st.header("Blogs")
        link = """
        <head>
        </head>
        <body>
        <a href="https://blogs.cdc.gov/niosh-science-blog/category/suicide/">Suicide Help</a> <br>
        <a href="https://www.govst.edu/suicide-prevention/">Why Is Suicide So Common Among College Students?</a> <br>
        <a href="https://www.helpguide.org/articles/suicide-prevention/suicide-prevention.htm">Suicide Prevention</a> <br>
        <a href="https://www.healthpartners.com/blog/suicide-prevention/">Suicide prevention: One simple question could save a life</a> <br>
        <a href="https://www.mentalwealthhub.com/blogs/suicide-awareness-blog/">Suicide Awareness</a> <br>
        <a href="https://www.sane.org/information-and-resources/the-sane-blog/suicide-prevention/fears-that-stop-the-question-are-you-okay">FEARS THAT STOP THE QUESTION ‘ARE YOU OKAY?’</a> <br>
        <a href="https://www.sane.org/information-and-resources/the-sane-blog/suicide-prevention/whats-the-value-of-ruok-day">WHAT'S THE VALUE OF RUOK DAY?</a> <br>
        </body>
        """
        st.markdown(link, unsafe_allow_html = True)        