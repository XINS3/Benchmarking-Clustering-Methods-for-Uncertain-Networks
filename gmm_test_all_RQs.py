# add by xin, 2026-05-13
from collections import defaultdict
import re

def natural_key(s):
    return [
        int(t) if t.isdigit() else t.lower()
        for t in re.split(r'(\d+)', s)
    ]

'''
# community strength RQ2
from Expected_mod import Trans_C1, APWP
import Expected_mod as ex 
import load_graph
import importlib
import bz2
import os 
import pandas as pd 
import json
import time
import networkx as nx 
importlib.reload(load_graph)
path='mcp_acp_data//k10_l10//result//gmm//'
#path2='datasets//' #comment by xin
path2='mcp_acp_data//k10_l10//' #add by xin
filelists=[i for i in os.listdir('mcp_acp_data//k10_l10//result//gmm')]
filelists.sort(key=natural_key)
T=[]
clustering=[]
value=[]
for file in filelists:
    print(file)
    graph=file[:-9]+'.txt'
    g=load_graph.read_g(path2+graph)
    edge=[]
    p=[]
    for u,v,w in g.edges(data=True):
        edge.append((u,v))
        p.append(w['weight'])

    with bz2.open(path+file,'rt') as f:
        data=json.load(f)
    # convert the table to dataframe
    #clustering_df=pd.DataFrame(data['tables']['clustering']) #comment by xin 2026-05-13
    #cluster=Trans_C1(list(clustering_df['clabel'])) #comment by xin
  
    clusters = defaultdict(list)
    for row in data["tables"]["clustering"]:
        #clusters[str(row["center"])].append(int(row["label"])) #comment by xin
        clusters[str(row["clabel"])].append(int(row["label"])) #add by xin
    cluster_list = list(clusters.values())
    data_acpc = {
        str(len(cluster_list)): cluster_list
    }
    cluster=list(data_acpc.values())[0]
 
    clustering.append(cluster)
    # Emod=ex.APWP(edge,p,cluster)
    # print('----------graph: ',graph,'----------')
    # print('cluster:',cluster)
    # print('-----------Ex modularity',Emod,'-----------')
    # value.append(Emod)
print('gmm',value)
    
from Expected_mod import Trans_C2
from sklearn.metrics.cluster import adjusted_mutual_info_score as ami

standard_c=[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
node=100
AMI=[]
for c in clustering:
    c=Trans_C2(c,node)
    
    score=ami(standard_c,c)
    print(score)
    AMI.append(score)
print(AMI)
'''

# number of clusters RQ3
'''
from Expected_mod import Trans_C1, APWP
import Expected_mod as ex 
import load_graph
import importlib
import time
import networkx as nx 
import bz2
import os 
import pandas as pd
import json
importlib.reload(load_graph)
from Expected_mod import Trans_C2
from sklearn.metrics.cluster import adjusted_mutual_info_score as ami 

path='mcp_acp_data//l10_p0.3//results//gmm_results//'
path2='mcp_acp_data//l10_p0.3//datasets//'
filelists=[i for i in os.listdir('mcp_acp_data//l10_p0.3//results//gmm_results')]
filelists.sort(key=natural_key)
print(filelists)
T=[]
clustering=[]
X_=[]
l=10
AMI=[]
for file in filelists:
    print(file)
    graph=file[:-9]+'.txt'
    g=load_graph.read_g(path2+graph)
   

    with bz2.open(path+file,'rt') as f:
        data=json.load(f)
    # convert the table to dataframe
    #clustering_df=pd.DataFrame(data['tables']['clustering']) #comment by xin 2026-05-13
    #cluster=Trans_C1(list(clustering_df['clabel'])) #comment by xin
  
    clusters = defaultdict(list)
    for row in data["tables"]["clustering"]:
        #clusters[str(row["center"])].append(int(row["label"])) #comment by xin
        clusters[str(row["clabel"])].append(int(row["label"])) #add by xin
    cluster_list = list(clusters.values())
    data_acpc = {
        str(len(cluster_list)): cluster_list
    }
    cluster=list(data_acpc.values())[0]

    strr=[]
    flag=0
   
    for _ in graph:
        if _=='k':
            
            flag=1
            continue
        if flag==0:
            continue
        if _<'0' or _>'9':
           
            break
        strr.append(_)
    
    k=sum([int(strr[i])*(10**(len(strr)-(i+1))) for i in range(len(strr))])
    c=[i for i in range(k*l)]
    
    stad_cluster=[c[x:x+l] for x in range(0, len(c), l)]
    ami_=ami(Trans_C2(stad_cluster,k*l),Trans_C2(cluster,k*l))
    AMI.append(ami_)
    X_.append(k)
print(AMI  )
print(X_)
'''

# shifting probability distribution graph RQ4
'''
from Expected_mod import Trans_C1, APWP
import Expected_mod as ex 
import load_graph
import importlib
import time
import networkx as nx 
import pandas as pd 
import json
import bz2
import os

importlib.reload(load_graph)
gmm_clustering={}
path1='mcp_acp_data//l10_k10_p0.4_multiplied//new//gmm_results//'
path2='mcp_acp_data//l10_k10_p0.4_multiplied//new//datasets//'
filelists=[i for i in os.listdir(path1) if i !='.DS_Store']
filelists.sort(key=natural_key)
T=[]
clustering=[]
value=[]
for file in filelists:
    print(file)
    file_list=file.split('_')
    strr=[]
    flag=0
   
    for _ in file:
        if _=='i':
            
            flag=1
            continue
        if flag==0:
            continue
        if _<'0' or _>'9':
           
            break
        strr.append(_)
    
    multi=str(0)+'.'+str(strr[1])#sum([int(strr[i])*(10**(len(strr)-(i+1))) for i in range(len(strr))])
    print(multi)
 
    
    graph=file[:-9]+'.txt'
    
    print('g',graph)
    g=load_graph.read_g(path2+graph)
    edge=[]
    p=[]
    for u,v,w in g.edges(data=True):
        edge.append((u,v))
        p.append(w['weight'])

    with bz2.open(path1+file,'rt') as f:
        data=json.load(f)
    # convert the table to dataframe
    #clustering_df=pd.DataFrame(data['tables']['clustering']) #comment by xin 2026-05-13
    #cluster=Trans_C1(list(clustering_df['clabel'])) #comment by xin
  
    clusters = defaultdict(list)
    for row in data["tables"]["clustering"]:
        #clusters[str(row["center"])].append(int(row["label"])) #comment by xin
        clusters[str(row["clabel"])].append(int(row["label"])) #add by xin
    cluster_list = list(clusters.values())
    data_acpc = {
        str(len(cluster_list)): cluster_list
    }
    cluster=list(data_acpc.values())[0]

    gmm_clustering.update({multi:cluster})
    print(cluster)
   
print(gmm_clustering)


import json
path='mcp_acp_data//l10_k10_p0.4_multiplied//new//gmm_results//'
with open(path+'gmm.json','w') as fp:
          json.dump(gmm_clustering,fp,indent=4) # With indent=4 (pretty format)
'''

# low probabilities RQ5
'''
from Expected_mod import Trans_C1, APWP
import Expected_mod as ex 
import load_graph
import importlib
import time
import networkx as nx 
import pandas as pd 
import json
import bz2
import os

importlib.reload(load_graph)
gmm_clustering={}
path1='datasets//l10_p0.3_evolving_lowP1//gmm_results//'
path2='datasets//l10_p0.3_evolving_lowP1//'
filelists=[i for i in os.listdir(path1)]
filelists.sort(key=natural_key)
T=[]
clustering=[]
value=[]
for file in filelists:
    file_list=file.split('_')
    k=[i for i in file_list if i[0]=='k'][0][1:]
    
    graph=file[:-9]+'.txt'
    print(graph)
    g=load_graph.read_g(path2+graph)
    edge=[]
    p=[]
    for u,v,w in g.edges(data=True):
        edge.append((u,v))
        p.append(w['weight'])

    with bz2.open(path1+file,'rt') as f:
        data=json.load(f)
    # convert the table to dataframe
    #clustering_df=pd.DataFrame(data['tables']['clustering']) #comment by xin 2026-05-13
    #cluster=Trans_C1(list(clustering_df['clabel'])) #comment by xin
  
    clusters = defaultdict(list)
    for row in data["tables"]["clustering"]:
        #clusters[str(row["center"])].append(int(row["label"])) #comment by xin
        clusters[str(row["clabel"])].append(int(row["label"])) #add by xin
    cluster_list = list(clusters.values())
    data_acpc = {
        str(len(cluster_list)): cluster_list
    }
    cluster=list(data_acpc.values())[0]

    gmm_clustering.update({k:cluster})
    print(cluster)
   
print(gmm_clustering)


import json
path='mcp_acp_data//l10_p0.3_evolving_lowP1//result//gmm//'
with open(path+'gmm_increaseK_lowP.json','w') as fp:
          json.dump(gmm_clustering,fp,indent=4) # With indent=4 (pretty format)
'''

# structure-aware/unaware RQ5

from Expected_mod import Trans_C1, APWP
import Expected_mod as ex 
import load_graph
import importlib
import time
import networkx as nx 
import pandas as pd 
import json
import bz2
import os
importlib.reload(load_graph)
gmm_clustering={}
path1='mcp_acp_data//l50_k2_p0.18_polarized_graph//result//gmm//'
path2='mcp_acp_data//l50_k2_p0.18_polarized_graph//datasets//'
filelists=[i for i in os.listdir(path1) if i !='.DS_Store' and i!='gmm_polarized.json']
filelists.sort(key=natural_key)
T=[]
clustering=[]
value=[]
for file in filelists:
    file_list=file.split('_')
    k=[i for i in file_list if i[0]=='k'][0][1:]
    name=file_list[-2]
    
    graph=file[:-9]+'.txt'
    print(graph)
    g=load_graph.read_g(path2+graph)
    edge=[]
    p=[]
    for u,v,w in g.edges(data=True):
        edge.append((u,v))
        p.append(w['weight'])

    with bz2.open(path1+file,'rt') as f:
        data=json.load(f)
    # convert the table to dataframe
    #clustering_df=pd.DataFrame(data['tables']['clustering']) #comment by xin 2026-05-13
    #cluster=Trans_C1(list(clustering_df['clabel'])) #comment by xin
  
    clusters = defaultdict(list)
    for row in data["tables"]["clustering"]:
        #clusters[str(row["center"])].append(int(row["label"])) #comment by xin
        clusters[str(row["clabel"])].append(int(row["label"])) #add by xin
    cluster_list = list(clusters.values())
    data_acpc = {
        str(len(cluster_list)): cluster_list
    }
    cluster=list(data_acpc.values())[0]

    gmm_clustering.update({name:cluster})
    print(cluster)
    Emod=ex.APWP(edge,p,cluster)
    # print('----------graph: ',graph,'----------')
    # print('cluster:',cluster)
    # print('-----------Ex modularity',Emod,'-----------')
    value.append(Emod)
   
print(value)


# import json
# path='mcp_acp_data//l50_k2_p0.18_polarized_graph//result//gmm//'
# with open(path+'gmm_polarized.json','w') as fp:
#           json.dump(gmm_clustering,fp,indent=4) # With indent=4 (pretty format)