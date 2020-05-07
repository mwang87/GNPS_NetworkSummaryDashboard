import dash
import dash_core_components as dcc
import dash_html_components as html
import networkx as nx
import random

def get_cosine_value(node):
    return random.random()

def get_histogram_cosine_value(G):
    output = {}
    for node in G.nodes(data = True):
        cosine_value = get_cosine_value(node)
        if output.__contains__(cosine_value*10//1/10):
            output[cosine_value*10//1/10] += 1
        else:
            output[cosine_value*10//1/10] = 1
    return output

G = nx.read_graphml('METABOLOMICS-SNETS-V2-1ad7bc36-download_cytoscape_data-main.graphml')

def generate_table(G):
    return html.Table([
        html.Thead(
            html.Tr(["number of nodes    ","    number of edges"])
        ),
        html.Tbody([
            html.Tr([G.number_of_nodes(),G.number_of_edges()])
        ])
    ])


external_stylesheets = ['https://urldefense.com/v3/__https://codepen.io/chriddyp/pen/bWLwgP.css__;!!Mih3wA!W1cpYR39OyzaI-RszMdP3tmdR1rd3LrG0i77vklPHzVZ6ScprLQBYBvBpLgt5ev1$ ']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='graphml stats'),
    generate_table(G)
])

if __name__ == '__main__':
    app.run_server(debug=True)




    
    
