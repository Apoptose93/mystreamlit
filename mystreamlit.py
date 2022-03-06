from components.csv_to_parquet import csv2parquet
from components.youtube_downloader import youtubeDownloader
import streamlit as st

from components.json_prettifier import json_pretty
from components.log_filter import log_filter 

def main():
    app_mode = st.sidebar.radio("# Choose mode",
    [
        "home",
        "log_filter",
        "json_prettifier",
        "csv2parquet",
        "youtube_downloader"
    ])
    if app_mode == "log_filter":
        log_filter()
    if app_mode == "json_prettifier":
        json_pretty()
    if app_mode == "csv2parquet":
        csv2parquet()
    if app_mode == "youtube_downloader":
        youtubeDownloader()

if __name__ == '__main__':
    main()