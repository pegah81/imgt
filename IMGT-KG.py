import streamlit as st
from assets.utils import load_css, image_to_base64

st.set_page_config(
    page_title="IMGT-KG",
    page_icon=":book:",
    layout="wide",
)

load_css('assets/styles.css')


# Profiles data
profiles = [
    {
        "avatar": "./Image/1571773098456.jpeg",
        "name": "Gaoussou Sanou",
        "statuts": ["PhD Student"],
        "linkedin": "https://www.linkedin.com/in/gaoussou-sanou-78982413b/",
        "affiliation": "UM, IGH, LIRMM",
        "mail": "gaoussou.sanou@igh.cnrs.fr",
    },
    {
        "avatar": "https://cdn-icons-png.flaticon.com/512/5577/5577995.png",
        "name": "Véronique Giudicelli",
        "statuts": ["Thesis Supervisor", "Research Engineer"],
        "linkedin": "https://www.linkedin.com/in/v%C3%A9ronique-giudicelli-b2559750/",
        "affiliation": "UM, IGH",
        "mail": "veronique.giudicelli@igh.cnrs.fr",
    },
    {
        "avatar": "https://cdn-icons-png.flaticon.com/512/5577/5577995.png",
        "name": "Patrice Duroux",
        "statuts": ["Thesis Supervisor", "Research Engineer"],
        "affiliation": "IGH",
        "mail": "patrice.duroux@igh.cnrs.fr",
    },
    {
        "avatar": "https://cdn-icons-png.flaticon.com/512/5577/5577995.png",
        "name": "Konstantin Todorov",
        "statuts": ["Thesis Co-Director", "Associate Professor"],
        "affiliation": "UM, LIRMM",
        "mail": "konstantin.todorov@lirmm.fr",
    },
    {
        "avatar": "https://cdn-icons-png.flaticon.com/512/5577/5577995.png",
        "name": "Sofia Kossida",
        "statuts": ["Thesis Co-director", "University Professor"],
        "linkedin": "https://www.linkedin.com/in/sofia-kossida-b235999/",
        "affiliation": "UM, IGH",
        "mail": "sofia.kossida@igh.cnrs.fr",
    }
]

# Main content area
st.markdown('<div class="container">', unsafe_allow_html=True)

# Title Card
st.markdown("""
    <div class="card">
        <div class="page-title">Welcome to IMGT Knowledge Graph (IMGT-KG): <span class="highlight">A knowledge graph to integrate immunogenetics data</span></div>
    </div>
""", unsafe_allow_html=True)

# Introduction Card
st.markdown("""
    <div class="card">
        <div class="card-title">Introduction</div>
        <div class="card-content">
            Considering the connected nature of immunogenetics entities from <strong>IMGT®</strong> <span style="color: green;">sequence</span> databases to the <span style="color: orange;">monoclonal antibodies</span> database,
            a need for integration of immunogenetics data arises. To cover this need, we built the <strong>IMGT Knowledge graph (IMGT-KG)</strong>, the first
            knowledge graph in the immunogenetics field. It bridges the gap between nucleotide and protein sequences of IMGT® databases and will open
            the way for effective queries and integrative immuno-omics analyses. <strong>IMGT-KG</strong> acquires data from <strong>IMGT®</strong>, then represents, describes and
            structures immunogenetics entities and their interrelationships in a knowledge graph using semantic web standards and technologies.
            <br>
            <br>
            <strong>IMGT-KG</strong> is built on top of an extended version of <strong>IMGT-ONTOLOGY</strong>. We prioritize reuse of existing terms in our knowledge graph as
            recommended by semantic web good practices. Many of these terms are from Open Biological and Biomedical Ontology
            <a href="https://obofoundry.org/" class="chip">(OBO)</a> Foundry ontologies (including Thesauris). <strong>IMGT-KG</strong> uses a set of rules to guide inferences on the positions
            of nucleotide sequences applying Allen Interval Algebra. <strong>IMGT-KG</strong> aims to describe immunogenetics entities from nucleotide level to the
            protein level. In addition, <strong>IMGT-KG</strong> provides external links to other resources including Protein Data Bank
            <a href="https://www.rcsb.org/" class="chip">(PDB)</a>, Immune Epitope Database
            <a href="https://www.iedb.org/" class="chip">(IEDB)</a> and <a href="https://pubmed.ncbi.nlm.nih.gov/" class="chip">PUBMED</a> articles.
        </div>
    </div>
    <br>
""", unsafe_allow_html=True)


st.markdown(f"""
    <div class="card">
        <img src="data:image/png;base64,{image_to_base64("./Image/IMGT-KG.png")}" class="card-img" alt="IMGT-KG">
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="card card-footer">
        We make openly and freely available <strong>IMGT-KG</strong> powered by
        <a href="https://yasgui.triply.cc/" class="chip">YASGUI</a> at this
        <a href="kgdata.html" class="chip">link</a> for the normal graph without inferences. In addition, we provide another way to access <strong>IMGT-KG</strong> including normal
        and inferred graph at this <a href="/fuseki/#/" class="chip">link</a> by the means of
        <a href="https://jena.apache.org/documentation/fuseki2/" class="chip">Apache Jena Fuseki2</a>.
    </div>
""", unsafe_allow_html=True)

# Abstract Card
st.markdown("""
    <div class="card">
        <div class="card-title">Abstract</div>
        <div class="card-content">
            Knowledge graphs are emerging as one of the most popular means for data federation, transformation, integration and sharing, promising
            to improve data visibility and reusability. Immunogenetics is the branch of life sciences that studies the genetics of the immune system.
            Although the complexity and the connected nature of immunogenetics data make knowledge graphs a prominent choice to represent and describe
            immunogenetics entities and relations, hence enabling a plethora of applications, little effort has been directed towards building and using
            such knowledge graphs so far. In this work, we present the IMGT Knowledge Graph (IMGT-KG), the first of its kind FAIR knowledge graph in
            immunogenetics. IMGT-KG acquires and integrates data from different immunogenetics databases, hence creating links between them.
            Consequently, IMGT-KG provides access to 79,670,110 triplets with 10,430,268 entities, 673 concepts and 173 properties. IMGT-KG reuses many
            existing terms from domain ontologies or vocabularies and provides external links to other resources of the same domain, as well as a set of
            rules to guide inference on nucleotide sequence positions by applying Allen Interval Algebra. Such inference allows, for example, reasoning
            about genomics sequence positions. IMGT-KG fills in the gap between genomics and protein sequences and opens a perspective to effective queries
            and integrative immuno-omics analyses. We make openly and freely available IMGT-KG with detailed documentation and a Web interface for
            access and exploration.
        </div>
        <div class="card-content">
            Sanou, G., Giudicelli, V., Abdollahi, N., Kossida, S., Todorov, K., Duroux, P. (2022).
            <a href="https://iswc2022.semanticweb.org/wp-content/uploads/2022/11/978-3-031-19433-7_36.pdf" class="chip">IMGT-KG: A Knowledge Graph for Immunogenetics</a>.
            In: , et al. The Semantic Web – ISWC 2022. ISWC 2022. Lecture Notes in Computer Science, vol 13489. Springer, Cham.
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

def display_team(profiles):
    st.markdown(
        """
            <h2 style="text-align: center;">Team</h2>
        """,
        unsafe_allow_html=True
    )
    
    linkedin_icon = "https://cdn-icons-png.flaticon.com/512/174/174857.png"  
    email_icon = "https://cdn-icons-png.flaticon.com/512/561/561127.png"
    affiliation_icon = image_to_base64("./Image/building2.png")

    for i, profile in enumerate(profiles):
        if i % 3 == 0: 
            cols = st.columns(3)
        
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="team_card">
                    <img src="{image_to_base64(profile['avatar'])}" class="team_img" alt="{profile['name']}">
                    <h3>{profile['name']}</h3>
                    <p class="email_background">
                        <img src="{email_icon}" class="profile_icon" alt="Email Icon"> 
                        <a href="mailto:{profile['mail']}">{profile['mail']}</a>
                    </p>
                    {(
                        f'<p><img src="{linkedin_icon}" class="profile_icon" alt="LinkedIn Icon"> '
                        f'<a href="{profile["linkedin"]}" target="_blank">LinkedIn</a></p>'
                    ) if 'linkedin' in profile else "<p></p>"}
                    <p>
                        <img src="{affiliation_icon}" class="profile_icon" alt="Email Icon">
                        {profile['affiliation']}
                    </p>
                </div>
                """, 
                unsafe_allow_html=True
            )


display_team(profiles)