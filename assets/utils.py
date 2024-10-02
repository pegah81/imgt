import streamlit as st
import base64
import os

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def image_to_base64(img_path, fallback_url="https://cdn-icons-png.flaticon.com/512/5577/5577995.png"):
    if not os.path.exists(img_path):
        return fallback_url  
    
    try:
        with open(img_path, "rb") as file_:
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
        return f"data:image/png;base64,{data_url}"  
    except Exception as e:
        return fallback_url
