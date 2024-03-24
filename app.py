import streamlit as st
import requests
import hashlib
from main import *

st.title("Check if your password has been leaked")

password = st.text_input("Enter your password:")

if st.button("Check"):
    result = mainf(password)
    st.title(result)
