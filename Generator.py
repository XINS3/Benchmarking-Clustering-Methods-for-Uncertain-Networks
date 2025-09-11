import networkx as nx
import matplotlib.pyplot as plt
import math
import random

#K = 12 # number of clusters
#l = 5 # size of clusters
def evolving(K,l,p,P):
    '''
    K: number of clusters
    l: size of clusters
    p: ratio of changing edges
    P: edge probabilities
    '''

    # Create an empty graph
    G = nx.Graph()

    # Create K copies of complete graph on l nodes and add them to G
    complete = nx.complete_graph(l)
    clusters = []
    for k in range(K):
        cluster = nx.relabel_nodes(complete, {i: l * k + i for i in range(l)})#relabel node id
        G = nx.compose(G, cluster)# compose complete graph
        clusters.append(cluster)# add complete graph

    N = len(G.nodes)
    M = len(G.edges)
    #low edge probability (0,0.1]
    #P=[random.uniform(0,0.1) for i in range(M)]
    #random.shuffle(P)
    # Change the edges
    for (u, v), w in zip(G.edges(), P):
        G[u][v]['weight'] = w
    k = 0
    for _ in range(int(p* M)):
        (I, J) = random.choice(list(clusters[k].edges)) #choose edge randomly from cluster k
        w = G[I][J]['weight']
        clusters[k].remove_edge(I, J) #remove edge from clusters
        G.remove_edge(I, J) #remove edge from G
        A = random.choice([I, J]) #random select one side of edge
        while(True):
            B = (l * (k + 1)  + random.randrange(l * (K - 1))) % N #random select another side from other clusters
            if A == B:
                continue
            if G.has_edge(A, B):
                continue
            G.add_edge(A, B,weight=w)
            break
        k += 1
        k %= K #keep k<K
   
    # wei=[]
    # g=nx.Graph()
    # edge=list(G.edges())
    # for i in range(len(edge)):
    #     wei.append((edge[i][0],edge[i][1],P[i]))
    # g.add_weighted_edges_from(wei)

    return G


from functools import reduce

def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


'''
same number of nodes, different number of clusters, same ratio (community structure)
k would change 

'''
def cluster_size(n,p):
    '''
    n: number of nodes
    p: ratio of changing edges
   
    '''
    # l is from n/2 to sqrt(n)
    fac=factors(n)
    L=[i for i in fac if i >=math.sqrt(n) and i <= n/2]
    print('L',L)
    graph=[]
    for l in L:

        # Create an empty graph
        G = nx.Graph()
        # Create K copies of complete graph on l nodes and add them to G
        complete = nx.complete_graph(l)
        print('n',n,'l',l,'k',n/l)
        K=int(n/l)
        clusters = []
        for k in range(K):
            cluster = nx.relabel_nodes(complete, {i: l * k + i for i in range(l)})#relabel node id
            G = nx.compose(G, cluster)# compose complete graph
            clusters.append(cluster)# add complete graph

        N = len(G.nodes)
        M = len(G.edges)
        #random edge probability
        #P=[random.random() for i in range(M)]

        #low edge probability (0,0.1]
        P=[random.uniform(0,0.01) for i in range(M)]
        random.shuffle(P)
        # Change the edges
        k = 0
        for _ in range(int(p* M)):
            (I, J) = random.choice(list(clusters[k].edges)) #choose edge randomly from cluster k
            clusters[k].remove_edge(I, J) #remove edge from clusters
            G.remove_edge(I, J) #remove edge from G
            A = random.choice([I, J]) #random select one side of edge
            while(True):
                B = (l * (k + 1)  + random.randrange(l * (K - 1))) % N #random select another side from other clusters
                if A == B:
                    continue
                if G.has_edge(A, B):
                    continue
                G.add_edge(A, B)
                break
            k += 1
            k %= K #keep k<K
    
        wei=[]
        g=nx.Graph()
        edge=list(G.edges())
        for i in range(len(edge)):
            wei.append((edge[i][0],edge[i][1],P[i]))
        g.add_weighted_edges_from(wei)
        graph.append((K,g))

    return graph 