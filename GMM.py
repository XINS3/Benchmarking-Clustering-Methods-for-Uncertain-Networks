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
    
    dist = {u: {v: inf for v in nodes} for u in nodes}
    for u, dd in nx.all_pairs_dijkstra_path_length(G, weight='weight'):
        dist[u].update(dd)

    for u in nodes:
        print('node: ',u,' ', dist[u])
    #dist=dict(nx.all_pairs_dijkstra_path_length(G,None,'weight'))
    
    mindist = {v: dist[centers[0]][v] for v in nodes}

    # pick centers greedly
    for _ in list(range(1,k)):
        next_center=max(mindist,key=lambda v: mindist[v])
        centers.append(next_center)
        
        for v in nodes:
            mindist[v]=min(mindist[v],dist[next_center][v])

    # assign nodes
    assigment={}
    max_distance=0
    for v in nodes:
        best_c,best_d=min(
            ((u,dist[u][v]) for u in centers),
            key=lambda x: x[1]
        )
        
        assigment[v]=best_c
        max_distance=max(max_distance,best_d)

    
    return centers,assigment,max_distance



