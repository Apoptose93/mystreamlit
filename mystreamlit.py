import streamlit as st

from components.json_prettifier import json_pretty
from components.log_filter import log_filter 

def main():
    app_mode = st.sidebar.radio("# Choose mode",
    [
        "home",
        "log_filter",
        "json_prettifier"
    ])
    if app_mode == "log_filter":
        log_filter()
    if app_mode == "json_prettifier":
        json_pretty()

if __name__ == '__main__':
    main()