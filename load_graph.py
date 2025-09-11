def loading_g(k,l,p,g,filename):
    '''
    k: number of clusters
    l: number of nodes in each cluster
    p: ratio between nodes within cluster and between cluster
    g: graph
    '''
    #evolving graph
    #filename='datasets//evolving_k'+str(k)+'_l'+str(l)+'_p'+str(p)+'.txt'
    with open(filename, 'w') as file:
    
        for u, v, w in g.edges(data=True):
            file.write(str(u) + ' '+str(v)+' '+str(w['weight'])+'\n')

def loading_P(filename):
    '''
    read edge prob. txt
    return P
    '''
    text_file = open(filename, "r")
    lines = text_file.read().split('\n')
    P=[]
    for i in lines:
        P.append(float(i))
    return P


def read_g(filename):
    import networkx as nx
    with open(filename, "r") as file:
        result = [[x for x in line.split()] for line in file]
    E=[]
    P=[]
    wei=[]
    for line in result:
        node1=int(line[0])
        node2=int(line[1])
        p=float(line[2])
        wei.append((node1,node2,p))
    g=nx.Graph()
    g.add_weighted_edges_from(wei)

    return g 

def read_graph_tool_g(filename):
    # read graph txt
    import graph_tool.all as gt 
    f = open(filename,'r')
    lines=[[n for n in x.split()] for x in f.readlines()]
    f.close()
    
    g = gt.Graph()
    lines_=[]
    for _ in lines:
        l=[]
        l.append(int(_[0]))
        l.append(int(_[1]))
        l.append(float(_[2]))
        lines_.append(l)
    
    g.add_vertex(1 + max([l[0] for l in lines_] + [l[1] for l in lines_]))
    property_map=g.new_edge_property('float')
    for l in lines_:
        g.add_edge(g.vertex(l[0]),g.vertex(l[1]))
        property_map[g.edge(g.vertex(l[0]),g.vertex(l[1]))]=l[2]
    return g,property_map




def save_P(filename,l,k):
    import random as rd
    P=[rd.random() for i in range(int(l*(l-1)/2*k))]
    rd.shuffle(P)
    #write P in txt 
    i=0
    with open(filename, 'w') as f:
        for line in P:
            f.write(f"{line}\n")
            i+=1
            if i==len(P)-1:
                break
        f.write(f"{line}")

def draw_g(K,l,G):
    import networkx as nx

    import matplotlib.pyplot as plt
    import math
    # Define custom positions for the vertices
    positions = {
        l * k + i: (
            math.sin(k / K * math.pi * 2) + math.sin(i / l * math.pi * 2) / K * 2,
            math.cos(k / K * math.pi * 2) + math.cos(i / l * math.pi * 2) / K * 2,
        ) for k in range(K) for i in range(l)
    }

    # Draw the graph with custom positions
    plt.figure(figsize=(8, 6))
    nx.draw(
        G, pos=positions, with_labels=True,
        node_color='lightgreen', node_size=800,
        edge_color='blue', font_weight='bold'
    )

    plt.title("Graph with"+str(K*l)+" Vertices")

    #plt.savefig(filename)
    plt.show()


def read_featured_matrix(filename,k,l):
    with open (filename) as file:
        data=file.readlines()
    t=[]
    X=[[] for i in range(k*l) ]
    flag=1# node int
    for line in data:
        t=line.split()
        
        for i in range(1,len(t)):
       
            X[int(t[0])].append(float(t[i]))
        
        t1=[]
    return X


        