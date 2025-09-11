# add one edge but delete the same edge, how to avoid this, if there is a smart way or just need an list to store all added edge.
# the set of edge probabilities are fixed, every time shuffle it. random prob.
def generate_complete_graph(k,l):
    import networkx as nx
    E=[]
    
    for i in range(k):
        g=nx.complete_graph(l)#each cluster is a complete graph
        for e in g.edges():
            n1=e[0]+i*l#add complete graph into big graph
            n2=e[1]+i*l#shift the node id
            E.append((n1,n2))
    return E

def return_graph(P,E,N):
    import networkx as nx
    wei=[]
   
    for i in range(len(P)):
        wei.append((E[i][0],E[i][1],P[i]))
        
    G=nx.Graph()
    #G.add_edges_from(E)
    G.add_weighted_edges_from(wei)
    G.add_nodes_from(list(range(N)))
    return G

def add_edge(l,k,current_cluster_id,E):
    import random
    while(True):#avoid multi-edges
        
        #current_cluster_id += 1
        if current_cluster_id >= k: current_cluster_id = 0
        next_cluster_id = current_cluster_id + 1
        if next_cluster_id >= k: next_cluster_id = 0
        current_node_from = random.randint(0,l-1)## random.randint(a,b) is from a to b instead of a to b-1
        current_node_from = current_cluster_id * l + current_node_from
        current_node_to = random.randint(0,l-1)
        current_node_to = next_cluster_id * l + current_node_to
        print('c_id',current_cluster_id)
        print((current_node_from,current_node_to),l*current_cluster_id,l*next_cluster_id)
        

        if ((current_node_from,current_node_to) not in E) and ((current_node_to,current_node_from) not in E):# avoid multi_edges
            break
    print('node id',current_node_from)
    return (current_node_from,current_node_to),current_cluster_id

def delete_random_nodes(current_node_from,k,E,l):
    import random
    print('current nodes neighbors are all newly added')
    # find the current cluster
    cluster_id=int(current_node_from/k)
    print(current_node_from,cluster_id)
    # choose two nodes in the cluster
    while(True):
        edge1=random.sample(list(range(cluster_id*l,(cluster_id+1)*l)),2)
        #check if edge in E
        node1=edge1[0]
        node2=edge1[1]
        
        if (node1,node2) in E or (node2,node1) in E :
            break
        
    return edge1
    

def delete_neighbor_edge(neigh_e,current_node_from,l,added_edge):
    import random
    while (True):#avoid delete the new edge
                
        choose_e=random.choice(neigh_e)
        if choose_e[0]==current_node_from:
            e_to=choose_e[1]
        else:
            e_to=choose_e[0]
        if max(current_node_from,e_to)-min(current_node_from,e_to)<l and choose_e not in added_edge:# check not delte new added edge
            break 
    
    return choose_e
    
def evoving_g(k,l,p,P):
    import networkx as nx
   
    import time
    import logging
    '''
    k: number of clusters
    l: number of nodes in each clusters
    p: ratio between edges within clusters and edges between clusters 0.5<=p<=1
    P: edge probabilities
    the potential problem is might have hub nodes, it's a bit slow
    '''
    #check
    #if p<0.5 or p>1:
     #   print('Error: input p is corssing the boundary!')
     #   return

    #generate k complete graphs
    E=generate_complete_graph(k,l)
    
    N=k*l
   
    m=len(E)
    delta_m=int((1-p)*m)+1#number of edges needed to be changed
    added_edge=[]#collect new added edge
    
    if p==1:#return disconnected component
     
        G=return_graph(P,E,N)

    t1=time.time()
    alpha=0 #control the nodes in specific cluster
    current_cluster_id = 0
    while(delta_m):
        for current_l in range(k):
            num=0
            
            for e_j in E:
                if e_j[0] in list(range(current_l*l,(current_l+1)*l)) and e_j[1] in list(range(current_l*l,(current_l+1)*l)):
                    num+=1
                    
            print('number of edges',num)
        #add an edge
        
         ## calculate the #nodes/cluster
       
        #choose a node 
        
        (current_node_from,current_node_to),current_cluster_id=add_edge(l,k,current_cluster_id,E)
        current_cluster_id += 1
        
        E.append((current_node_from,current_node_to))    
        #print(delta_m)
        added_edge.append((current_node_from,current_node_to))

        #delete an edge
        print('current node',current_node_from)
        #find the node's neighbor
        neigh_e=[e for e in E if current_node_from in e]
        #logging.info(neigh_e)
        # check current_node_from degree if equals to 1, and the only one is the new added.
        # check if current_node_from neighbors are all newly-added
        flag=1
        for current_e in neigh_e:
            if current_e not in added_edge:
                flag=0
                
        if len(neigh_e)==1 or flag==1:
            #logging.INFO('current node only have newly added neighbors!')
            (node1,node2)=delete_random_nodes(current_node_from,k,E,l)
            print('edges that choosed to be deleted in random_delete way',(node1,node2))
            #logging.debug('edges that choosed to be deleted ',str((node1,node2)))
            E.remove((node1,node2))
            

            
            #print('jump out third loop!')
            #print('delete edge',edge1)

        else:
            #print('randomly choose current nodes neighbors')
            #logging.info('randomly choose one neighbor edge of current node!')
            choose_e=delete_neighbor_edge(neigh_e,current_node_from,l,added_edge)
            #logging.info('edges that choosed to be deleted',str(choose_e))
            print('edges that choosed to be deleted in nodes neighbor',str(choose_e))
            #logging.debug(choose_e in E)
            E.remove(choose_e)
        delta_m-=1
        print(delta_m)
        alpha+=1
       
    t2=time.time()

    print('loops need ',t2-t1,'sec')
    #P=[random.random() for i in range(len(E))]
    #random.shuffle(P)
    G=return_graph(P,E,N)
 
    return G
        

