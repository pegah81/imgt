import streamlit as st
from assets.utils import load_css, image_to_base64

st.set_page_config(
    page_title="IMGT-KG",
    page_icon=":book:",
    layout="wide",
)

load_css('assets/styles.css')

# Main content area
st.markdown('<div class="container">', unsafe_allow_html=True)

# Title Card
st.markdown("""
    <div class="card">
        <div class="page-title">IMGT-KG Documentation</div>
    </div>
""", unsafe_allow_html=True)


st.markdown("""
    <div class="card">
        <div class="card-content">
           The VoID description file of IMGT-KG file is available
            <a href="void.ttl" class="chip">here</a>
            in turtle format.
            <br>
        </div>
    </div>
    <br>
""", unsafe_allow_html=True)