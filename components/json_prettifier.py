import streamlit as st 

def json_pretty():
    text = st.text_input(label = "input json",value ={"your": "json"})
    st.json(text)

    st.sidebar.text("sidebar json")