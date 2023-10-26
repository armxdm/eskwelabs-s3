# General Libraries
import pickle
import pandas as pd

# Model deployment
import streamlit as st

#model = pickle.load(open('gb_tk.pkl', 'rb'))

st.title("Eskwelabs S3 Recommender Project")
st.caption("by: Team Swifthrees")

st.divider()
#adding a selectbox
choice = st.text_input(
    "Enter Input:")

st.button("Submit", type="primary")