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
        <div class="page-title">IMGT-KG Description</div>
    </div>
""", unsafe_allow_html=True)


# Introduction Card
st.markdown("""
    <div class="card">
        <div class="card-title">Introduction</div>
        <div class="card-content">
            The <strong>IMGT-KG</strong> data model can be divided into five levels of description, 
            from nucleotide to protein sequence. The initial level comprises the depiction of genes 
            and alleles. The subsequent level provides details about the genomic loci of these genes. 
            The following level describes the sequence characteristics of the genes. The fourth level 
            transitions to the protein level, presenting a description pertaining to the sequence of the 
            protein chain and its domains. Finally, the last model describes the chain that belongs to the 
            structure. In the data model, every class has an annotation label 
            <a href="http://www.w3.org/2000/01/rdf-schema#label" class="chip">(rdfs:label)</a>, a definition 
            <a href="http://www.w3.org/2004/02/skos/core#definition" class="chip">(skos:definition)</a>
            and a comment <a href="http://www.w3.org/2000/01/rdf-schema#comment" class="chip">(rdfs:comment)</a> when it is possible. 
            A dinamyc visualisation of the data model made with 
            <a href="https://visjs.github.io/vis-network/" class="chip">Vis-Network</a> is provided. However a table with additional annotation properties is provided, 
            when they exist.
        </div>
        <br>
        <div class="code-block">
            PREFIX rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt; <br>
            PREFIX faldo: &lt;http://biohackathon.org/resource/faldo#&gt; <br>
            PREFIX skos: &lt;http://www.w3.org/2004/02/skos/core#&gt; <br>
            PREFIX obo: &lt;http://purl.obolibrary.org/obo/&gt; <br>
            PREFIX : &lt;http://www.imgt.org/imgt-ontology#&gt; <br>
        </div>
    </div>
""", unsafe_allow_html=True)


# Gene Level
st.markdown("""
    <div class="card">
        <div class="card-title">Gene Level</div>
        <div class="card-content">
            At the gene level, we have a Gene which can be member of 
             <a href="http://purl.obolibrary.org/obo/RO_0002350" class="chip">(obo:RO_0002350)</a>
            Group, that could be a member of a SubGroup and/or Clan. A Clan or a SubGroup can also be member of a Group. A Gene concept is defined by a gene type (variable, diversity ...) and a structure type. An allele is a gene variant that is associated with it. An Allele has a functionality type that indicates its functionality (functional,pseudogene...) and it is associated to a sequence region 
             <a href="http://biohackathon.org/resource/faldo#Region" class="chip">(faldo:Region)</a>
            , which can be a reference or literature sequence. Every Gene is ordered in a Locus and belongs to a taxon 
             <a href="http://purl.obolibrary.org/obo/NCBITaxon_1" class="chip">(obo:NCBITaxon_1)</a>
            .
        </div>
    </div>
    <br>
""", unsafe_allow_html=True)

# Table
html_table_1 = """
<table class='table-1'>
    <thead>
        <tr>
            <th> </th>
            <th>AnnotationProperty</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">Gene</td>
        </tr>
        <tr>
            <td>imgt_link</td>
            <td>a link that points to imgt website</td>
        </tr>
        <tr>
            <td rowspan="4">Allele</td>
        </tr>
        <tr>
            <td>has_fcode</td>
            <td>a code for functionality type</td>
        </tr>
        <tr>
            <td>has_number</td>
            <td>number of Allele</td>
        </tr>
    </tbody>
</table>
"""

st.markdown(html_table_1, unsafe_allow_html=True)


# Locus Level
st.markdown("""
    <div class="card">
        <div class="card-title">Locus Level</div>
        <div class="card-content">
            A Locus belongs to a taxon with a location type that indicates its location (major locus, orphon ...). It is part of 
            <a href="http://purl.obolibrary.org/obo/BFO_0000050" class="chip">(obo:BFO_0000050)</a>
            chromosome 
            <a href="http://purl.obolibrary.org/obo/SO_0000340" class="chip">(obo:SO_0000340)</a>
            . Each chromosome is member of a given assembly 
            <a href="http://purl.obolibrary.org/obo/SO_0001248" class="chip">(obo:SO_0001248)</a>
            which has a version number 
            <a href="http://purl.obolibrary.org/obo/SWO_0004000" class="chip">(obo:SWO_0004000)</a>
            , data origin 
            <a href="http://purl.obolibrary.org/obo/NCIT_C103167" class="chip">(obo:NCIT_C103167)</a>
            and belongs also to a taxon.
        </div>
    </div>
    <br>
""", unsafe_allow_html=True)


# Sequence Level
st.markdown("""
    <div class="card">
        <div class="card-title">Sequence Level</div>
        <div class="card-content">
            The sequence level characterizes the features of the sequence. A feature is a sequence region which is associated with a location, and a label. 
            Therefore, each region has a label and a location 
            <a href="http://biohackathon.org/resource/faldo#ExactPosition" class="chip">(faldo:ExactPosition)</a> with a start and end positions. 
            A region at the nucleotide sequence level is part of 
            <a href="http://purl.obolibrary.org/obo/BFO_0000050" class="chip">(obo:BFO_0000050)</a> a DNA or RNA sequence 
            <a href="http://purl.obolibrary.org/obo/GENO_0000960" class="chip">(obo:GENO_0000960)</a> with an accession number 
            <a href="http://purl.obolibrary.org/obo/NCIT_C25402" class="chip">(obo:NCIT_C25402)</a>. 
            A region can be a prototype entity or a cluster (A DNA fragment covering several genomic entities). 
            The Cluster and the prototype entity are part of a biological sequence 
            <a href="http://purl.obolibrary.org/obo/GENO_0000702" class="chip">(obo:GENO_0000702)</a> thanks to 
            isPrototypeInSeq and isClusterInSeq relation, respectively. 
            The biological sequence contains other regions which are related to each other. 
            Every region in the same biological sequence has an 
            <a href="https://en.wikipedia.org/wiki/Allen%27s_interval_algebra#:~:text=Allen's%20interval%20algebra%20is%20a,about%20temporal%20descriptions%20of%20events." class="chip">Allen interval relationship</a>, 
            for example, a region A can be next to (adjacent) to other regions.
        </div>
    </div>
    <br>
""", unsafe_allow_html=True)


# Second Table

# Table
html_table_2 = """
 <table class='table-1'>
    <thead>
        <tr>
            <th> </th>
            <th>AnnotationProperty</th>
            <th>Description</th>
        </tr>
    </thead>    
    <tbody>
        <tr>
            <td rowspan="4">Region</td>
        </tr>
        <tr>
            <td>has_nucleotide_sequence</td>
            <td>composition in nucleotides of the region when it's a coding region</td>
        </tr>
        <tr>
            <td>has_imgt_qualifier</td>
            <td>a qualifier imgt to describe the region</td>
        </tr>
        <tr>
            <td rowspan="2">has_nucleotide_sequence</td>
        </tr>
        <tr>
            <td>obo:GENO_0000960</td>
            <td>composition in nucleotides of the sequence</td>
        </tr>
    </tbody>
</table>
"""

st.markdown(html_table_2, unsafe_allow_html=True)


# Chain Level
st.markdown("""
    <br>
    <div class="card">
        <div class="card-title">Chain Level</div>
        <div class="card-content">
            This level is the transition from nucleotide sequences to protein sequences. A chain
            <a class="chip" href="http://purl.obolibrary.org/obo/NCIT_C41207">obo:NCIT_C41207</a> can have protein domains
            <a class="chip" href="http://purl.obolibrary.org/obo/NCIT_C13303">obo:NCIT_C13303</a> with a domain type. It also has regions and residues
            <a class="chip" href="http://purl.obolibrary.org/obo/NCIT_C48795">obo:NCIT_C48795</a> with the associated amino acids
            <a class="chip" href="http://purl.obolibrary.org/obo/CHEBI_33709">obo:CHEBI_33709</a> and an IMGT numbering. Each chain and domain have a label and a location. The associated region of a Chain is the reference sequence
            of an Allele with a similarity score. The Chains belong to a taxon and a structure
            <a class="chip" href="http://purl.obolibrary.org/obo/NCIT_C13303">obo:NCIT_C13303</a>.
        </div>
    </div>
    <br>
""", unsafe_allow_html=True)


html_table_3 = """
    <table class="table-1">
        <thead>
            <tr>
                <th> </th>
                <th>AnnotationProperty</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="4">Chain</td>
            </tr>
            <tr>
                <td>code4A</td>
                <td>code of the chain</td>
            </tr>
            <tr>
                <td>has_imgt_chain_description</td>
                <td>a description of the chain in its different domains</td>
            </tr>
            <tr>
                <td>imgt_link</td>
                <td>a link that points to imgt website</td>
            </tr>
            <tr>
                <td rowspan="3">Domain</td>
            </tr>
            <tr>
                <td>has_imgt_collier_perles</td>
                <td>imgt collier de perles link</td>
            </tr>
            <tr>
                <td>has_sheet</td>
                <td>different sheets of domain</td>
            </tr>
            <tr>
                <td rowspan="4">Residue</td>
            </tr>
            <tr>
                <td>abreviation</td>
                <td>short name or abreviation of the residue</td>
            </tr>
            <tr>
                <td>has_phi_angle</td>
                <td>phi angle</td>
            </tr>
            <tr>
                <td>has_psi_angle</td>
                <td>psi angle</td>
            </tr>
        <tbody>
    </table>
"""

st.markdown(html_table_3, unsafe_allow_html=True)


# Structure Level
st.markdown("""
    <div class="card">
        <div class="card-title">Structure Level</div>
        <div class="card-content">
            A Structure 
            <a class="chip" href="http://purl.obolibrary.org/obo/NCIT_C13303">obo:NCIT_C13303</a> can belong to a crystal structure 
            <a class="chip" href="http://semanticscience.org/resource/SIO_001100">sio:SIO_001100</a>, has a label and a molecular component. 
            A Structure is attached to an entry of amino acid sequence 
            <a class="chip" href="http://purl.obolibrary.org/obo/GENO_0000720">obo:GENO_0000720</a>. This sequence has an accession number, 
            a related bibliographic reference, and the acquisition experiment.
        </div>
    </div>
    <br>
""", unsafe_allow_html=True)

# Table
st.markdown("""
    <table class='table-1'>
        <thead>
            <tr>
                <th></th>
                <th>AnnotationProperty</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="5">Structure</td>
            </tr>
            <tr>
                <td>common_name</td>
                <td>common name</td>
            </tr>
            <tr>
                <td>commercial_name</td>
                <td>commercial name</td>
            </tr>
            <tr>
                <td>inn_name</td>
                <td>INN name</td>
            </tr>
            <tr>
                <td>immune_epitope</td>
                <td>an external link that points to the predict epitope of a structure in IEDB</td>
            </tr>
            <tr>
                <td rowspan="8">Amino acid sequence</td>
            </tr>
            <tr>
                <td>contact_analysis</td>
                <td>a link that points to pair contacts analyses</td>
            </tr>
            <tr>
                <td>has_amino_sequence</td>
                <td>amino acid sequence</td>
            </tr>
            <tr>
                <td>imgt_link</td>
                <td>a link that points to IMGT website</td>
            </tr>
            <tr>
                <td>interaction_paratope_epitope</td>
                <td>a link that points to interaction paratope epitope</td>
            </tr>
            <tr>
                <td>is_entry_from</td>
                <td>amino sequence's database</td>
            </tr>
            <tr>
                <td>jmol_visualisation</td>
                <td>a link to explore the structure in Jmol</td>
            </tr>
            <tr>
                <td>pdb_link</td>
                <td>a external link to pdb database</td>
            </tr>
            <tr>
                <td rowspan="5">Article</td>
            </tr>
            <tr>
                <td>dc:title</td>
                <td>article's title</td>
            </tr>
            <tr>
                <td>dc:contributor</td>
                <td>article's contributors</td>
            </tr>
            <tr>
                <td>dc:date</td>
                <td>publication date</td>
            </tr>
            <tr>
                <td>has_journal</td>
                <td>journal of publication</td>
            </tr>
        </tbody>
    </table>
""", unsafe_allow_html=True)

# IMGT-KG Statistics
st.markdown("""
    <div class="card">
        <div class="card-title">IMGT-KG Statistics</div>
        <div class="card-content">
            <strong>IMGT-KG</strong> provides access to 79,670,110 triplets without inferences, 
            95,508,660 triplets with inferences applied, 10,430,268 entities, 
            15,848,105 distinct subjects, 21,861,727 distinct objects, 
            673 distinct concepts or classes, and 171 distinct properties or relations. 
            We provide below figures demonstrating the main features of 
            <strong>IMGT-KG</strong>.
        </div>
    </div>
    <br>
""", unsafe_allow_html=True)