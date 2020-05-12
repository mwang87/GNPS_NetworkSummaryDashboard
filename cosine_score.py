import plotly.express as px
import pandas as pd
import requests
import networkx as nx

G = nx.read_graphml('METABOLOMICS-SNETS-V2-1ad7bc36-download_cytoscape_data-main.graphml')
df ={"cosine_score":[]}
for edge in G.edges(data = True):
    df["cosine_score"].append(edge[2]["cosine_score"])

fig = px.histogram(df,x= "cosine_score")
fig.show()


