import streamlit as st 

if __name__ == '__main__':
    x = st.slider("Select a value")
    st.write(x, "squared is", x*x)