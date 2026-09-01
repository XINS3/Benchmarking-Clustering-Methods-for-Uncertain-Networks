from Expected_mod import Trans_C1, Trans_C2

import load_graph
import importlib
import bz2
import os 
import pandas as pd 
import json
import time
import networkx as nx 
importlib.reload(load_graph)

from sklearn.metrics.cluster import adjusted_mutual_info_score as ami
#path='mcp_acp_data//k10_l10//result//acpc//' # xin delete for checking revision
path='mcp_acp_data//k10_l10//result//acpc//temp_result//' # xin add for checking revision
path2='datasets//l10_k10//'
filelists=[i for i in os.listdir(path)]
filelists.sort()
T=[]
clustering=[]
value=[]
for file in filelists:
    print(file)
    graph=file[:-9]+'.txt'
    print('graph',graph)
    g=load_graph.read_g(path2+graph)
    edge=[]
    p=[]
    for u,v,w in g.edges(data=True):
        edge.append((u,v))
        p.append(w['weight'])

    with bz2.open(path+file,'rt') as f:
        data=json.load(f)
    # convert the table to dataframe
    #print(data['tables']['clustering'])
    clustering_df=pd.DataFrame(data['tables']['clustering'])
    
 
    print(Trans_C1(list(clustering_df['clabel'])),len(Trans_C1(list(clustering_df['clabel']))))
    print(list(clustering_df['probability']))

    cluster=Trans_C1(list(clustering_df['clabel']))
    clustering.append(cluster)


standard_c=[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
node=100
AMI=[]
for c in clustering:
    c=Trans_C2(c,node)
    
    score=ami(standard_c,c)
    print(score)
    AMI.append(score)
print(AMI)


    