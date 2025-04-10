import pandas as pd
import requests
import streamlit as st

from api.preprocessing import clean_text


st.title("Tag prediction APP", anchor=None, help=None)
st.header("Predict Stackoverflow questions tags", anchor=None, help=None)

text = st.text_input(label="Enter your question:")
text = clean_text(text)

if text:
    res = requests.get("http://127.0.0.1:5000/api/text=" + text)
    if res.status_code == 200:
        res = res.json()
        st.write(pd.DataFrame(dict(res))["tags"].values)

    else:
        st.write("Error: Unable to fetch data from the API.")
else:
    st.write("Please enter a programming question.")
