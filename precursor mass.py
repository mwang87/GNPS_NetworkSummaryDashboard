import plotly.express as px
import pandas as pd
import requests
import networkx as nx

G = nx.read_graphml('METABOLOMICS-SNETS-V2-1ad7bc36-download_cytoscape_data-main.graphml')
df ={"precursor mass":[]}

for node in G.nodes(data = True):
    df["precursor mass"].append(node[1]["precursor mass"])
fig = px.histogram(df,x = "precursor mass")
fig.show()


