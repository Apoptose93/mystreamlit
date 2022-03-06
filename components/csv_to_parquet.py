from io import StringIO
import streamlit as st 
import pandas as pd
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def csv2parquet():
   uploaded_file = st.file_uploader("Choose a file")
   if uploaded_file is not None:
    #    # To read file as bytes:
    #    bytes_data = uploaded_file.getvalue()
    #    st.write(bytes_data)

    #    # To convert to a string based IO:
    #    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    #    # To read file as string:
    #    string_data = stringio.read()

       # Can be used wherever a "file-like" object is accepted:
       dataframe = pd.read_csv(uploaded_file)
       st.write(dataframe)
       parquet = dataframe.to_parquet(compression='snappy')
       st.download_button(
          label="Download data as PARQUET",
          data=parquet,
          file_name='data.parquet'
 )





