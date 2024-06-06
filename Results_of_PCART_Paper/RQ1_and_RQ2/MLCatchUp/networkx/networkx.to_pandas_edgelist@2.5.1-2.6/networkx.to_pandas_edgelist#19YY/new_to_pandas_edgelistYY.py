import networkx as nx
import pandas as pd
G = nx.gnp_random_graph(5, 0.5)
edgelist_df = nx.to_pandas_edgelist(G, source='source', target='target', nodelist=None, dtype=None, edge_key=None)