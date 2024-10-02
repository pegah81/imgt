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
        <div class="page-title">IMGT/MAB-KG Access</div>
    </div>
""", unsafe_allow_html=True)


# Markdown content for the IMGT/MAB-KG data access page
st.markdown("""
    <div class="card">
        <div class="card-content">
            This page provide the access to <strong>IMGT/MAB-KG</strong> data. The interface is powered by 
            <a href="https://yasgui.triply.cc/" class="chip">YASGUI</a>
            , you can directly access to 
            <a href="https://imgt.org/fuseki/#/dataset/MabkgKg/query" class="chip">IMGT/MAB-KG SPARQL Endpoint Server directly</a>
            which uses 
            <a href="https://jena.apache.org/documentation/fuseki2/" class="chip">Apache Jena Fuseki</a>
            as SPARQL server and 
            <a href="https://jena.apache.org/documentation/tdb2/" class="chip">Apache Jena TDB</a>
            as triplestore. It provides acces to the IMGT/MAB-KG data. Some examples are provided below.
            <br>
        </div>
    </div>
    <br>
""", unsafe_allow_html=True)

# Title Card
st.markdown("""
    <div class="card">
        <div class="page-title">IMGT/MAB-KG Data Access</div>
    </div>
""", unsafe_allow_html=True)