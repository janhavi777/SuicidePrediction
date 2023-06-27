import sys
sys.path.append("/opt/anaconda3/lib/python3.9/site-packages")

import streamlit as st
from PIL import Image

def show_helpline_page():

    image = Image.open("suicideprevention_ribbon.png")
    st.image(image, width=200)

    st.header("Emergency Helpline")
    st.subheader(f"Emergency Toll free number: 1800-599-0019")

    link = """
    <head>
    </head>
    <body>
    <a href="https://findahelpline.com/">Find a Helpline</a> <br>
    </body>
    """
    st.markdown(link, unsafe_allow_html = True)


