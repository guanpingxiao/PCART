import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4)])
centrality = nx.betweenness_centrality(G, normalized=True, weight=None, k=None, seed=None)