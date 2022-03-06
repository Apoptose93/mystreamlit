from io import BytesIO, StringIO
from components.utils import generate_zip, getVideoAsBufferMP3, getVideoAsBufferMP4
import streamlit as st 
import pytube
import pandas as pd
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def getPlaylist(input, datatype) -> list:
    playlist = pytube.Playlist(input)
    my_bar = st.progress(0)
    progress = -0.0001
    videos_files = []
    for url in playlist.video_urls:
        if datatype == "mp3":
            videos_files.append(getVideoAsBufferMP3(url))
        if datatype == "mp4":
            videos_files.append(getVideoAsBufferMP4(url))
        # update progress bar
        progress += 1/len(playlist.video_urls)
        my_bar.progress(progress)
    return playlist.title, videos_files

def getVideo(url, datatype) -> list:
    if datatype == "mp3":
        data = getVideoAsBufferMP3(url)
    if datatype == "mp4":
        data = getVideoAsBufferMP4(url)
    title = data[0]
    return title, [data]

def downloadData(input, datatype: str):
    try:
        try:
            title, video_files = getPlaylist(input, datatype)
        except:
            title, video_files = getVideo(input, datatype)    

        zip_data = generate_zip(video_files)
        st.download_button(
            label=f"Download {title}",
            data = zip_data,
            file_name = f"{title}.zip"
        )

    except Exception as e:
        st.error(f"{e}, Invalid URL")

def youtubeDownloader():
    input = st.text_input("URL")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Download Video or Playlist as MP3"):
            downloadData(input,"mp3")
    with col2:
        if st.button("Download Video or Playlist"):
            downloadData(input,"mp4")