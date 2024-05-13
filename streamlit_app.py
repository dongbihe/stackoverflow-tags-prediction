import pandas as pd
import requests
import streamlit as st

st.title("Tag prediction APP", anchor=None, help=None)
st.header("Predict Stackoverflow questions tags", anchor=None, help=None)

text = st.text_input(label="Enter your question:")

if text:
    res = requests.get("http://127.0.0.1:5000/api/text=" + "".join(text))
    # print(res)
    if res.status_code == 200:
        res = res.json()
        # st.write((type(dict(res))))
        # st.write(pd.DataFrame(dict(res))['tags'].values)
        st.write(pd.DataFrame(dict(res))["tags"].values)
        # st.write(pd.DataFrame(dict(res))['tags'].values[1])
        # st.write(res['tags'])
        # res = pd.read_json(res)
    else:
        st.write("Error: Unable to fetch data from the API.")
else:
    st.write("Please enter a programming question.")
