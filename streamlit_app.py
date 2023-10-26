# General Libraries
import pickle
import pandas as pd

# Model deployment
from flask import Flask
import streamlit as st

#model = pickle.load(open('gb_tk.pkl', 'rb'))

st.title("Eskwealabs S3")

#adding a selectbox
choice = st.text_input(
    "Enter Input:")

st.button("Submit")