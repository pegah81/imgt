import streamlit as st
from assets.utils import load_css


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
        <div class="page-title">IMGT-KG Access</div>
    </div>
""", unsafe_allow_html=True)

# IMGT-KG Data Access Information
st.markdown("""
    <div class="card">
        <div class="card-content">
            This page provides access to <span class="strong-emphasis">IMGT-KG</span> data. The interface is powered by
            <span class="chip"><a href="https://yasgui.triply.cc/" class="chip-link">YASGUI</a></span>. You can access the
            <span class="chip"><a href="/fuseki/#/dataset/ImgtKg/query" class="chip-link">IMGT-KG SPARQL Endpoint Server directly</a></span>, which uses
            <span class="chip"><a href="https://jena.apache.org/documentation/fuseki2/" class="chip-link">Apache Jena Fuseki</a></span> as the SPARQL server and
            <span class="chip"><a href="https://jena.apache.org/documentation/tdb2/" class="chip-link">Apache Jena TDB</a></span> as the triplestore. 
            It provides access to the <span class="strong-emphasis">IMGT-KG</span> data. Some examples are provided below.
        </div>
    </div>
    <br>
""", unsafe_allow_html=True)



sparql_items = [
    {
        "text": "Find information on the genes/alleles functionality and why they are not functional in the case of a pseudogene, for example.",
        "req": "Queries/Query_scenario_1.rq"
    },
    {
        "text": "Explore crystal structures and the associated external links including epitote on IEDB, PUBMED article, PDB link and Jmol visualisation.",
        "req": "Queries/Query_scenario_2.rq"
    },
    {
        "text": "Find the COVID-19 spike protein with the associated chains, genes, alleles and genomics reference sequences.",
        "req": "Queries/Query_scenario_3.rq"
    },
    {
        "text": "Select an Allele which is partial and for which there exists a complete literature sequence.",
        "req": "Queries/Query1.rq"
    },
    {
        "text": "Find why a gene is pseudogene based on its functionality qualifier.",
        "req": "Queries/Query2.rq"
    },
    {
        "text": "Select genes which have not a given feature: L-PART-1, for example.",
        "req": "Queries/Query3.rq"
    },
    {
        "text": "Select groups, genes, alleles and their CDR3-IMGT length.",
        "req": "Queries/Query4.rq"
    },
    {
        "text": "Select pseudogenes without L-PART-1.",
        "req": "Queries/Query5.rq"
    },
    {
        "text": "Select chains and their alleles with allele properties.",
        "req": "Queries/Query6.rq"
    },
    {
        "text": "More thorough way to describe a chain and its association with an allele.",
        "req": "Queries/Query7.rq"
    },
    {
        "text": "Unification of nucleotide sequences (genomics) and amino acid sequences (proteins).",
        "req": "Queries/Query8.rq"
    },
    {
        "text": "Selection of structures with their bibliographic reference (is there always one, or there might be more than one?) and the external link to IEDB and Pubmed. Additional structure properties can be retrieved (chains, label …).",
        "req": "Queries/Query9.rq"
    },
    {
        "text": "Retrieve crystal structures and their related annotations including external links (jmol visualisation, imgt_display, pdb ... ).",
        "req": "Queries/Query10.rq"
    },
    {
        "text": "Description of a particular chain (chain-1QLFA).",
        "req": "Queries/Query11.rq"
    },
]

    
st.markdown('<link href="https://cdn.jsdelivr.net/npm/@mdi/font/css/materialdesignicons.min.css" rel="stylesheet">', unsafe_allow_html=True)

st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="page-title">SPARQL Query Examples</div>
        </div>
    </div>
""", unsafe_allow_html=True)

for item in sparql_items:
    st.markdown(
        f"""
        <div class='query-item-example'>
            <span class='icon' style='font-size: 24px; vertical-align: middle;'>
                <i class='mdi mdi-database-search-outline'></i>
            </span> 
            {item['text']}
        </div>
        """,
        unsafe_allow_html=True
    )
