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
        <div class="page-title">IMGT/MAB-KG, the IMGT-KG for Monoclonal Antibodies</div>
    </div>
""", unsafe_allow_html=True)


st.markdown("""
    <div class="card">
        <div class="card-content">
            <p>
                Monoclonal antibodies (mAbs) are proteins made in the laboratory that act as natural antibodies.
                They bind specifically to certain targets in the body and stimulate the immune system. The mechanisms of action of mAbs range from detection and destruction of target cells,
                stimulation of immune-mediated cell toxicity, to modulation of the immune system. The mAbs can also carry drugs or radiation to efficiently deliver cell-killing agents to target cells. 
                In order to provide a unique and valuable resource concerning mAbs with therapeutic application, <strong>IMGT&reg;</strong> has developed IMGT/mAb-DB, a database that contains standardized descriptions about mAbs, 
                their targets, clinical indications, and other characteristics.
            </p>
            <br>
            <p>
                From an immunogenetics data integration perspective, we built the first FAIR immunogenetics knowledge graph, <strong>IMGT Knowledge Graph (IMGT-KG)</strong> to bridge the gap between nucleotide and protein sequences of
                IMGT® databases. In this same perspective, we built <strong>IMGT/MAB-KG</strong>, the IMGT-KG for therapeutic monoclonal antibodies, using semantic web standards and technologies. 
                <strong>IMGT/MAB-KG</strong> is a specific part of IMGT-KG that represents, describes, and structures all knowledge of therapeutic mAbs.
                It is intrinsically connected to the IMGT-KG and reuses terms and relationships from 
                <span class="chip"><a href="http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#" class="chip-link">NCIT</a></span>, 
                <span class="chip"><a href="https://mondo.monarchinitiative.org/" class="chip-link">MONDO</a></span>, and some resources of the Open Biological and Biomedical Ontology 
                <span class="chip"><a href="https://obofoundry.org/" class="chip-link">OBO</a></span>.
            </p>
        </div>
    </div>
    <br>
""", unsafe_allow_html=True)

eye_icon = """
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="white" viewBox="0 0 24 24"><path d="M12 5c-7.633 0-11 7-11 7s3.367 7 11 7 11-7 11-7-3.367-7-11-7zm0 12c-2.761 0-5-2.239-5-5s2.239-5 5-5 5 2.239 5 5-2.239 5-5 5zm0-8c-1.657 0-3 1.343-3 3s1.343 3 3 3 3-1.343 3-3-1.343-3-3-3z"/></svg>
"""

st.markdown(f"""
    <div class="card">
        <div class="card-title">IMGT/MAB-KG Schema Description</div>
        <div class="card-content">
            <p class="text-body-2">
                The data model is built as an extended version of IMGT-ONTOLOGY, described in our previous 
                <span class="chip"><a href="https://iswc2022.semanticweb.org/wp-content/uploads/2022/11/978-3-031-19433-7_36.pdf" class="chip-link">publication</a></span>.
                Here, we describe only the core elements including concepts and object properties.
            </p>
            <p class="text-body-2">
                The data model of <strong>IMGT/MAB-KG</strong> presents several parts, the core element being the monoclonal antibody represented by a pharmacological substance and an INN molecule (International nonproprietary names).
                The INN molecule is associated with a receptor that binds to a target, which belongs to a taxon, has a construct that consists of one or many segments. 
                The construct and its segments have an IMGT label.
            </p>
            <p class="text-body-2">
                It also has bibliographical references, a clinical domain, a mechanism of action, and its effects. The Pharmacological Substance may have a biosimilar, an origin clone, and an associated product.
                The monoclonal antibody product is produced by a company and has one or more clinical trials. Every clinical trial has a clinical phase and a clinical indication for a disease, which belongs to a clinical domain.
            </p>
            <p class="text-body-2">
                A clinical trial can be the subject of a decision by an organization with a final status. The pharmacological Substance may be linked to <strong>IMGT-KG</strong> 3D structure elements.
            </p>
            <br>
        </div>
        <div style="display: flex; justify-content: center;">
            <button class="green-button">
                <span style="font-size: inherit; font-family: inherit;">{eye_icon} Vizualisation of the Monoclonal Antibodies Knowledge graph schema </span>
            </button>
        </div>
    </div>
""", unsafe_allow_html=True)

# Example of a monoclonal antibody: Relatlimab
st.markdown(f"""
<div class="container">
    <div class="card">
        <div class="card-title">Example of a monoclonal antibody: Relatlimab (mAb_781)</div>
        <div class="card-content">
            <p class="text-body-2">
                We instantiate our data model with the mAb 781 Relatlimab, we include all levels and all information within Relatlimab.
            </p>
        </div>
        <div style="display: flex; justify-content: center;">
            <button class="green-button">
                <span style="font-size: inherit; font-family: inherit;">{eye_icon} Visualization all information concerning Relatlimab (mAb_781) </span>
            </button>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# Relatlimab (mAb_781)
st.markdown(f"""
    <div class="card">
        <div class="card-title">Relatlimab (mAb_781)</div>
        <div class="card-content">
            <p class="text-body-2">
                The monoclonal antibody mAb_781 is an INN molecule, Relatlimab, which appears in the INN proposed list 119 (for the year 2018) and in the recommended list 81 (for the year 2019).
                It has the inn number 10735, which is associated to an <strong>IMGT-KG</strong> structure with the accession number 10735. Its INN name is relatlimab and has been found in 32 studies (clinical trials).
                It is associated to the IgG4-Kappa_781 receptor and two products: Product_Bristol-Myers_Squiibb_781 and Product_Onno_Pharmaceuicals_Co.Ltd_781. It has also a mechanism of action MOA_781_oncology_blocking.
                The mAb_781 has also external links to 
                <span class="chip">
                    <a href="https://www.pharmgkb.org/" class="chip-link">pharmgkb</a>
                </span>, these links include the PharmGKB identifier associated to the monoclonal antibody and all the properties associated to 
            </p>
        </div>
        <div style="display: flex; justify-content: center;">
            <button class="green-button">
                <span style="font-size: inherit; font-family: inherit;">{eye_icon}  Visualization of Relatlimab (mAb_781) </span>
            </button>
        </div>
    </div>
""", unsafe_allow_html=True)


# Receptor of Relatlimab (mAb_781): IGg4-Kappa_781
st.markdown(f"""
    <div class="card">
        <div class="card-title">Receptor of Relatlimab (mAb_781): IGg4-Kappa_781</div>
        <div class="card-content">
            <p class="text-body-2">
                The mAb receptor is an immunoglobulin: IgG4-Kappa and has a format associated with it.
                The IgG4-Kappa_781 receptor targets the lymphocyte activating 3,
                <span class="chip">
                    <a href="https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6476" class="chip-link">HGNC:6476</a>
                </span> that belongs to the taxon Homo sapiens,
                and it has an external link to PharmGKB.
            </p>
        </div>
        <div style="display: flex; justify-content: center;">
            <button class="green-button">
                <span style="font-size: inherit; font-family: inherit;">{eye_icon}  Visualization of the receptor of Relatlimab (mAb_781): IGg4-Kappa_781 </span>
            </button>
        </div>
    </div>
""", unsafe_allow_html=True)


# Mode of action of Relatlimab (mAb_781)
st.markdown(f"""
    <div class="card">
        <div class="card-title">Mode of action of Relatlimab (mAb_781)</div>
        <div class="card-content">
            <p class="text-body-2">
                The mode of action MOA_781_oncology_blocking has clinical domain oncology with a definition that describes the action of the mAb.
                It has a blocking mechanism and has an immunostimulant effect.
                The MOA_781_oncology_blocking has a bibliographic reference <a href="https://pubmed.ncbi.nlm.nih.gov/33925565/">PM33925565</a> and also image associated.
            </p>
        </div>
        <div style="display: flex; justify-content: center;">
            <button class="green-button">
                <span style="font-size: inherit; font-family: inherit;">{eye_icon}  Visualization of the mode of action of Relatlimab (mAb_781): MOA_781_oncology_blocking</span>
            </button>
        </div>
    </div>
""", unsafe_allow_html=True)

# Product of Relatlimab (mAb_781)
st.markdown(f"""
    <div class="card">
        <div class="card-title">Product of Relatlimab (mAb_781)</div>
        <div class="card-content">
            <p class="text-body-2">
                The commercial product, Product_Bristol-Myers_Squiibb_781, has the common names BMS-986016, ONO-4482, relatlimab-rmbw and the proprietary name OPDUALAGTM. It was developed by Bristol-Myers_Squiibb and has different clinical trials. For instance, we represent
                the StudyProduct_Bristol-Myers_Squibb_Mesothelioma_781 which indicates that this mAb is studied in the treatment of mesothelioma disease, in clinical phase II and was designed as an orphan drug by FDA on 2017-08-18.
            </p>
        </div>
        <div style="display: flex; justify-content: center;">
            <button class="green-button">
                <span style="font-size: inherit; font-family: inherit;">{eye_icon}  Visualization of the product of Relatlimab (mAb_781): Product_Bristol-Myers_Squiibb_781 </span>
            </button>
        </div>
    </div>
</div>

""", unsafe_allow_html=True)