import sys
sys.path.append("/opt/anaconda3/lib/python3.9/site-packages")

import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from article_page import show_article_page
from reference_page import show_reference_page
from helpline_page import show_helpline_page


page = st.sidebar.selectbox("Select", ("Predict", "Explore", "Articles", "References", "Emergency Helpline"))

if page == "Explore":
    show_explore_page()
elif page == "Articles":
    show_article_page()
elif page == "References":
    show_reference_page()
elif page == "Emergency Helpline":
    show_helpline_page()
else:
    show_predict_page()