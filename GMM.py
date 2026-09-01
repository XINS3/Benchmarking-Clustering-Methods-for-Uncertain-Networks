import networkx as nx

def read_txt_to_graph(path):
    G = nx.Graph()
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            u, v, w = line.split()
            u = int(u)
            v = int(v)
            w = float(w)

            # 直接把 probability 当 weight
            G.add_edge(u, v, weight=w)

    return G
def gmm(G, k):
    import networkx as nx 
    import random
    import math
    '''
    pick k centers greedily 
    select v that nearest to centers
    '''
    inf=math.inf
    nodes=list(G.nodes)
    weight=[]
    edge=[]
    for u,v,w in G.edges(data=True):
        weight.append(w['weight'])
        edge.append((u,v))
    centers=[random.choice(nodes)]
    print('initial center: ',centers)
    
    dist = {u: {v: inf for v in nodes} for u in nodes}
    for u, dd in nx.all_pairs_dijkstra_path_length(G, weight='weight'):
        dist[u].update(dd)
    
    #for u in nodes:
    #    print('node: ',u,' ', dist[u])
    #dist=dict(nx.all_pairs_dijkstra_path_length(G,None,'weight'))
    
    mindist = {v: dist[centers[0]][v] for v in nodes}
    #print('initial mindist: ',mindist)
    # pick centers greedly
    for _ in list(range(1,k)):
        next_center=max(mindist,key=lambda v: mindist[v])
        centers.append(next_center)
        print('next center: ',next_center)
        for v in nodes:
            mindist[v]=min(mindist[v],dist[next_center][v])
        #print('mindist: ',mindist)

    # assign nodes
    assigment={}
    max_distance=0
    for v in nodes:
        best_c,best_d=min(
            ((u,dist[u][v]) for u in centers),
            key=lambda x: x[1]
        )
        #print('node: ',v,' best center: ',best_c,' distance: ',best_d)
        assigment[v]=best_c
        max_distance=max(max_distance,best_d)

    
    return centers,assigment,max_distance



from collections import defaultdict
import json

def assignment_to_clusters(assignment):
    clusters = defaultdict(list)

    for node, center in assignment.items():
        clusters[center].append(node)

    # 转成 list of clusters
    cluster_list = list(clusters.values())

    return cluster_list

def save_clusters_json(cluster_list, output_path):
    data = {
        len(cluster_list): cluster_list
    }

    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph", required=True, help="input txt graph file")
    parser.add_argument("-k", "--clusters", type=int, required=True, help="number of clusters")
    parser.add_argument("-o", "--output", required=True, help="output json file")
    parser.add_argument("--seed", type=int, default=None, help="random seed")

    args = parser.parse_args()

    G = read_txt_to_graph(args.graph)

    centers, assignment, max_d = gmm(G, args.clusters)

    cluster_list = assignment_to_clusters(assignment)

    save_clusters_json(cluster_list, args.output)

    print("clusters:", len(cluster_list))
    print("max_distance:", max_d)
    print("saved to:", args.output)