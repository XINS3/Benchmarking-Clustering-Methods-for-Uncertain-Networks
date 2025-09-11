# add one edge but delete the same edge, how to avoid this, if there is a smart way or just need an list to store all added edge.
# the set of edge probabilities are fixed, every time shuffle it. random prob.
def evoving_g(k,l,p,P):
    import networkx as nx
    import random
    import time
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
    E=[]
    
    for i in range(k):
        g=nx.complete_graph(l)#each cluster is a complete graph
        for e in g.edges():
            n1=e[0]+i*l#add complete graph into big graph
            n2=e[1]+i*l#shift the node id
            E.append((n1,n2))
    
    N=k*l
   
    m=len(E)
    delta_m=int((1-p)*m)+1#number of edges needed to be changed
    added_edge=[]#collect new added edge
    if p==1:#return disconnected component
     
        wei=[]
   
        for i in range(len(P)):
            wei.append((E[i][0],E[i][1],P[i]))
           
        G=nx.Graph()
        #G.add_edges_from(E)
        G.add_weighted_edges_from(wei)
        G.add_nodes_from(list(range(N)))
        return G

    t1=time.time()

    while(delta_m):
        #add an edge
        alpha=0 #control the nodes in specific cluster
         ## calculate the #nodes/cluster
        #for current_l in range(k):
         #   num=0
            
          #  for e_j in E:
           #     if e_j[0] in list(range(current_l*l,(current_l+1)*l)) and e_j[1] in list(range(current_l*l,(current_l+1)*l)):
           #         num+=1
           # print('number of edges',num)
        #choose a node 
        #current_cluster_id = -1
        while(True):#avoid multi-edges
            
            current_node_from=random.randint(0,1000)%l+alpha*l
            if current_node_from<(k-1)*l:
                
                current_node_to=random.randint(0,1000)%l+(alpha+1)*l
            else:
                alpha=0
                current_node_to=random.randint(0,1000)%l+alpha*l
            '''
            current_cluster_id += 1
            if current_cluster_id == k: current_cluster_id = 0
            next_cluster_id = current_cluster_id + 1
            if next_cluster_id == k: next_cluster_id = 0
            current_node_from = random.randint(0,l)
            current_node_from = current_cluster_id * l + current_node_from
            current_node_to = random.randint(0,l)
            current_node_to = next_cluster_id * l + current_node_to
            '''

            if ((current_node_from,current_node_to) not in E) and ((current_node_to,current_node_from) not in E):# avoid multi_edges
                break
            #print((current_node_from,current_node_to) ,'E',E)
        #print('jump out first loop!')
        #print('add edge',(current_node_from,current_node_to))
        E.append((current_node_from,current_node_to))    
        #print(delta_m)
        added_edge.append((current_node_from,current_node_to))

        #delete an edge

        #find the node's neighbor
        neigh_e=[e for e in E if current_node_from in e]
        # check current_node_from degree if equals to 1, and the only one is the new added.
        # check if current_node_from neighbors are all newly-added
        flag=1
        for current_e in neigh_e:
            if current_e not in added_edge:
                flag=0
                
        if len(neigh_e)==1 or flag==1:
            print('current nodes neighbors are all newly added')
            # find the current cluster
            cluster_id=int(current_node_from/k)
            # choose two nodes in the cluster
            while(True):
                edge1=random.sample(list(range(cluster_id*l,(cluster_id+1)*l)),2)
                #check if edge in E
                node1=edge1[0]
                node2=edge1[1]
               
                if (node1,node2) in E or (node2,node1) in E :
                    break
            if (node1,node2) in E:
                E.remove((node1,node2))
            else:
                E.remove((node2,node1))

            
            #print('jump out third loop!')
            #print('delete edge',edge1)

        else:
            #print('randomly choose current nodes neighbors')
            while (True):#avoid delete the new edge
                
                choose_e=random.choice(neigh_e)
                if choose_e[0]==current_node_from:
                    e_to=choose_e[1]
                else:
                    e_to=choose_e[0]
                if max(current_node_from,e_to)-min(current_node_from,e_to)<l and choose_e not in added_edge:# check not delte new added edge
                    break 
                #print('e_to',e_to)
            #print('jump out second loop!')   
            #print('delete edge',choose_e)
            E.remove(choose_e)
        delta_m-=1
        print(delta_m)
        #alpha+=1
       
    t2=time.time()

    print('loops need ',t2-t1,'sec')
    #P=[random.random() for i in range(len(E))]
    #random.shuffle(P)
    wei=[]
   
    for i in range(len(P)):
        wei.append((E[i][0],E[i][1],P[i]))
       
    G=nx.Graph()
    #G.add_edges_from(E)
    G.add_weighted_edges_from(wei)
    G.add_nodes_from(list(range(N)))
    
   

    return G
        

