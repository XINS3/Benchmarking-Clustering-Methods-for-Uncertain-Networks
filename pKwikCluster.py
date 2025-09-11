#!/usr/bin/env python3

import networkx as nx
import sys
import random

#assert int(nx.__version__.split('.')[0]) == 2, 'Networkx version 2 is required'

def load(path):
    G = nx.read_edgelist(path, data=[('probability', float)])
    return G


def pKwikCluster(graph):
    clusters = []
    # Filter edges with probability less than 0.5
   # valid_edges = [(u, v) for u, v, d in graph.edges(data='probability')
    #               if d >= 0.5]
    #G = nx.Graph(valid_edges)
    #print('Filtered graph has',G.number_of_nodes(),
    #      'nodes and', G.number_of_edges(), 'edges',
    #      file=sys.stderr)
    pro={}
    for u,v,d in graph.edges(data=True):
        pro[(u,v)]=d['weight']
       
    while graph.number_of_nodes() > 0:
        root = random.choice(list(graph.nodes))
        star = list(graph.neighbors(root))
        c=[]
        for u in star:
            if (u,root) in list(graph.edges):
               
                if pro[(u,root)]>0.5:
                    c.append(u)
            else:
                if pro[(root,u)]>0.5:
                    c.append(u)

        cluster = [root] + c
        clusters.append(cluster)
       
        graph.remove_nodes_from(cluster)
    return clusters


if __name__ == '__main__':
    G = load(sys.argv[1])
    print('loaded graph with',G.number_of_nodes(),
          'nodes and', G.number_of_edges(), 'edges',
          file=sys.stderr)
    clusters = pKwikCluster(G)
    print(clusters)




