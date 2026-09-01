#!/usr/bin/env python3

import networkx as nx
import sys
import random

#assert int(nx.__version__.split('.')[0]) == 2, 'Networkx version 2 is required'

def load(path):
    G = nx.read_edgelist(path, data=[('weight', float)])
    return G


def pKwikCluster(graph, threshold=0.5, seed=None):
    if seed is not None:
        random.seed(seed)

    G = graph.copy()
    clusters = []

    while G.number_of_nodes() > 0:
        root = random.choice(list(G.nodes()))
        cluster_neighbors = []

        for v in G.neighbors(root):
            if G[root][v]['weight'] > threshold:
                cluster_neighbors.append(v)

        cluster = [root] + cluster_neighbors
        clusters.append(cluster)
        G.remove_nodes_from(cluster)

    return clusters


if __name__ == '__main__':
    G = load(sys.argv[1])
    print('loaded graph with',G.number_of_nodes(),
          'nodes and', G.number_of_edges(), 'edges',
          file=sys.stderr)
    clusters = pKwikCluster(G)
    print(clusters)




