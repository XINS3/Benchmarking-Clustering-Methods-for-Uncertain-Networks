def APWP(edge,p,c):
    from  DFT_cpp import dft
    
    '''
    input:
    edge: list form : [(1,2),(2,3),(4,5)]
    p: edge probabilities, list form : [0.2,0.4,0.5]
    c: clustering, form list / dictionary [[0,3,4],[1,2]] / {[0,3,4],[1,2]}
    
    output:
    approximated expected modularity
    '''
   

    # initialize expected modularity
    
    S=0
    
    #interate cluster (community) by cluster (community)
    
    for cluster in c:
        
    #edges in the cluster
    
        E_c_in=[]
        
    #edge possibilities in the cluster
    
        Ep_c_in=[]
        
    #edges between the cluster
    
        E_c_bet=[]
        
    #edge possibilities in the cluster
    
        Ep_c_bet=[]
        
    #edges outside the cluster
    
        E_c_out=[]
        
    #edge posibilities in the cluster
    
        Ep_c_out=[]
  
        for i in range(len(edge)):
            edge_node1=edge[i][0]
            edge_node2=edge[i][1]
            
            # collect edges completely within community c
            
            if edge_node1 in cluster and edge_node2 in cluster:
                E_c_in.append(edge[i])
                Ep_c_in.append(p[i])
            
            # collect edges between community c
            
            elif edge_node1 in cluster or edge_node2 in cluster:
                E_c_bet.append(edge[i])
                Ep_c_bet.append(p[i])
                
            # collect edges outside community c
            
            else:
                E_c_out.append(edge[i])
                Ep_c_out.append(p[i])
        
        
        # #edges in ec,ecc_,ec_
        
        N_E_c=len(E_c_in)+1
        N_E_bet=len(E_c_bet)+1
        N_E_out=len(E_c_out)+1
        
        
        # probabilities of ec, ecc_, ec_ in one partition
        # use discrete fourier transform to approximate
        
        P1=[]
        for i in range(N_E_c):
            P1.append(dft(i,Ep_c_in))
        P2=[]
        for i in range(N_E_bet):
            P2.append(dft(i,Ep_c_bet))
        P3=[]
        for i in range(N_E_out):
            P3.append(dft(i,Ep_c_out))
        
        Sum=0
        
        # calculate expected modularity
        
        for i in range(N_E_c):
            if N_E_c==0:
                ec=0
                p1=1
            else:
           
                 ec=i
               
                 p1=P1[ec]
                
                

            for j in range(N_E_bet):
                if N_E_bet==0:
                    ecc_=0
                    p2=1
                else:
                   
                    ecc_=j
                   
                    p2=P2[ecc_]
                    
                   
                   
                   
                for k in range(N_E_out):
                    if N_E_out==0:
                        ec_=0
                        p3=1
                    else:
                       
                        ec_=k
                       
                        p3=P3[ec_]
                        
                       
                    
                    # the graph is an empty graph:
                    
                    if ec==0 and ecc_==0 and ec_==0:
                        Sum+=0
                    else:
                       
                        Sum+=(ec/((ec+ecc_+ec_))-((2*ec+ecc_)**2/(4*(ec+ecc_+ec_)**2)))*p1*p2*p3

                      
            
        S+=Sum   
        
    return S
    
            
           


# In[37]:



def PWP(edge,p,c):
    from Probabilities import PB
    

    

    # initialize excepted modularity
    S=0
    
    #interate cluster (community) by cluster (community)
    
    for cluster in c:
       
    #edges in the cluster
    
        E_c_in=[]
        
    #edge possibilities in the cluster
    
        Ep_c_in=[]
        
    #edges between the cluster
    
        E_c_bet=[]
        
    #edge possibilities in the cluster
    
        Ep_c_bet=[]
        
    #edges outside the cluster
    
        E_c_out=[]
        
    #edge posibilities in the cluster
    
        Ep_c_out=[]

        
        
        for i in range(len(edge)):
            edge_node1=edge[i][0]
            edge_node2=edge[i][1]
            
            # collect edges completely within community c
            
            if edge_node1 in cluster and edge_node2 in cluster:
                E_c_in.append(edge[i])
                Ep_c_in.append(p[i])
                
            # collect edges between community c
            
            elif edge_node1 in cluster or edge_node2 in cluster:
                E_c_bet.append(edge[i])
                Ep_c_bet.append(p[i])
                
            # collect edges outside community c
            
            else:
                E_c_out.append(edge[i])
                Ep_c_out.append(p[i])
        
       
        # #edges in ec,ecc_,ec_
        
        N_E_c=len(E_c_in)+1
        N_E_bet=len(E_c_bet)+1
        N_E_out=len(E_c_out)+1
        
        # probabilities of ec, ecc_, ec_ in one partition
        # use definition of poisson binomial distribution
        
        P1=[]
        for i in range(N_E_c):
            P1.append(PB(i,Ep_c_in))
        P2=[]
        for i in range(N_E_bet):
            P2.append(PB(i,Ep_c_bet))
        P3=[]
        for i in range(N_E_out):
            P3.append(PB(i,Ep_c_out))
        
        Sum=0
        
        # calculate expected modularity
        
        for i in range(N_E_c):
            if N_E_c==0:
                ec=0
                p1=1
            else:
           
                 ec=i
                
                 p1=P1[ec]
                
            for j in range(N_E_bet):
                if N_E_bet==0:
                    ecc_=0
                    p2=1
                else:
                   
                    ecc_=j
                   
                    p2=P2[ecc_]
                    
                   
                  
                for k in range(N_E_out):
                    if N_E_out==0:
                        ec_=0
                        p3=1
                    else:
                       
                        ec_=k
                       
                        p3=P3[ec_]
                       
                    
                    # when the graph is empty
                    
                    if ec==0 and ecc_==0 and ec_==0:
                        Sum+=0
                    else:
                       
                        Sum+=(ec/((ec+ecc_+ec_))-((2*ec+ecc_)**2/(4*(ec+ecc_+ec_)**2)))*p1*p2*p3
                       
            
        S+=Sum   
        
    return S
    
            
        


# In[44]:



def Trans_C1(c):
    import numpy as np
    '''
    change sequences to clustering
    c=[0,1,1,3] to c=[[0],[1,2],[3]]
    this function can be used in PWP and APWP's parameter 'c'
    
    input:
    c: c=[0,1,1,3]
    node: #nodes (int)
    
    output:
    c_nodes: c=[[0],[1,2],[3]]
    
    '''

    c_nodes=[]
    
    #tag visit or not
    
    c_novisit=[]
    
    for i in range(len(c)):
        
        # using hash to initialize community to not visit
        
        c_novisit.append([c[i],0])
        
    for i in range(len(c)):
        
        # when community ID not be visited:
        
        if c_novisit[i][1]==0:
            cc=[]
            cc.append(i)
            c_novisit[i][1]=-1
            for j in range(i+1,len(c)):
                if c[i]==c[j] and c_novisit[j][1]==0:
                    cc.append(j)
                    c_novisit[j][1]=-1
            c_nodes.append(cc)
    return c_nodes


# In[45]:


def Trans_C2(c_nodes,node):
    import numpy as np
    
    '''
    change clustering to sequences
    c=[[0],[1,2],[3]] to c=[0,1,1,3]
    this function can be used in brute force and sampling's parameter 'c'
    
    input:
    c_nodes: c=[[0],[1,2],[3]]
    node: #nodes (int)
    
    output:
    c: c=[0,1,1,3]
    
    '''
    
    c=np.zeros(node)
    for i in range(len(c_nodes)):
        
        
        for j in range(len(c_nodes[i])):
            c[list(c_nodes[i])[j]]=int(i)
      
        
    return c