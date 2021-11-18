import streamlit as st 

def log_filter():
    text = st.text_input(label = "input json",value ={"your": "json"})
    log_list = text.split("\n")
    error_list = ["ERROR", "error"]
    log_filtered = [n for n in log_list if any(m in n for m in error_list)]
    output = "\n ------------------------------ \n".join(log_filtered)
    st.write(output)
