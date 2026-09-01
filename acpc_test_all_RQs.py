# function that replace Tcl().call('lsort','-dict',filelists) for natural sorting of file names
# add by xin, 2026-05-13
from collections import defaultdict
import re

def natural_key(s):
    return [
        int(t) if t.isdigit() else t.lower()
        for t in re.split(r'(\d+)', s)
    ]


#Expected modularity according to the different community strengths -RQ2

'''below is added by xin 2026-05-13'''
   
'''
from Expected_mod import Trans_C1, APWP
import Expected_mod as ex 
import load_graph
import importlib
import bz2
import os 
import pandas as pd 
import json
from collections import defaultdict
importlib.reload(load_graph)
path='mcp_acp_data//k10_l10//result//acpc//'
#path2='datasets//' #comment by xin
path2='mcp_acp_data//k10_l10//' #add by xin
filelists=[i for i in os.listdir('mcp_acp_data//k10_l10//result//acpc')]
filelists.sort()
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
 
    print(file,'----------graph: ',graph,'----------')
    #print('cluster:\n',cluster)
    
    
    clustering.append(cluster)


    Emod=ex.APWP(edge,p,cluster)
    print('----------graph: ',graph,'----------')
    print('cluster:',cluster)
    print('-----------Ex modularity',Emod,'-----------')
    value.append(Emod)
print('mod',value)

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

# number of clusters. -RQ3

'''

import os

from Expected_mod import Trans_C1, APWP
import Expected_mod as ex 
import load_graph
import importlib
import time
import bz2
import pandas as pd 
import json
from collections import defaultdict
from Expected_mod import Trans_C2
from sklearn.metrics.cluster import adjusted_mutual_info_score as ami 

importlib.reload(load_graph)
path='mcp_acp_data//l10_p0.3//results//acpc_results//'
path2='mcp_acp_data//l10_p0.3//datasets//'
filelists=[i for i in os.listdir('mcp_acp_data//l10_p0.3//results//acpc_results//')]
filelists.sort()
print(filelists)
T=[]
clustering=[]
X_=[]
l=10
NMI=[]
for file in filelists:
    print(file)
    graph=file[:-9]+'.txt'
    g=load_graph.read_g(path2+graph)
   

    with bz2.open(path+file,'rt') as f:
        data=json.load(f)
    # convert the table to dataframe
    #clustering_df=pd.DataFrame(data['tables']['clustering']) #comment by xin 2026-05-13

    #cluster=Trans_C1(list(clustering_df['clabel'])) #comment by xin 2026-05-13

    #below add by xin 2026-05-13
    clusters = defaultdict(list)
    for row in data["tables"]["clustering"]:
        #clusters[str(row["center"])].append(int(row["label"])) #comment by xin
        clusters[str(row["clabel"])].append(int(row["label"])) 
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
    nmi_=ami(Trans_C2(stad_cluster,k*l),Trans_C2(cluster,k*l))
    NMI.append(nmi_)
    X_.append(k)
print(X_)
print(NMI)
'''

# shifting probabilities -RQ4
'''
from collections import defaultdict

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
#from tkinter import Tcl
from os import listdir
importlib.reload(load_graph)



acpc_clustering={}
path1='mcp_acp_data//l10_k10_p0.4_multiplied//new//acp_results//'
path2='mcp_acp_data//l10_k10_p0.4_multiplied//new//datasets//'
filelists=[i for i in os.listdir(path1) if i !='.DS_Store']
#print(filelists)
#filelists=Tcl().call('lsort','-dict',filelists) #comment by xin
filelists.sort(key=natural_key) #add by xin 2026-05-13
T=[]
clustering=[]
value=[]
print(filelists)
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
    print(strr)
    multi=str(0)+'.'+str(strr[1])#sum([int(strr[i])*(10**(len(strr)-(i+1))) for i in range(len(strr))])
    print(multi)
 
    
    graph=file[:-9]+'.txt'
    
    #print('g',graph)
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

    #below add by xin 2026-05-13
    clusters = defaultdict(list)
    for row in data["tables"]["clustering"]:
        #clusters[str(row["center"])].append(int(row["label"])) #comment by xin
        clusters[str(row["clabel"])].append(int(row["label"])) 
    cluster_list = list(clusters.values())
    data_acpc = {
        str(len(cluster_list)): cluster_list
    }
    cluster=list(data_acpc.values())[0]
    acpc_clustering.update({multi:cluster})
    print(cluster)
   
print(acpc_clustering)
 
# saving

import json
path='mcp_acp_data//l10_k10_p0.4_multiplied//new//acp_results//'
with open(path+'acpc.json','w') as fp:
          json.dump(acpc_clustering,fp,indent=4) # With indent=4 (pretty format)
'''

# low probability edges -RQ5
'''
from collections import defaultdict

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
#from tkinter import Tcl
from os import listdir
importlib.reload(load_graph)
acpc_clustering={}
path1='mcp_acp_data//l10_p0.3_evolving_lowP1//result//acpc//'
path2='mcp_acp_data//l10_p0.3_evolving_lowP1//dataset//'
filelists=[i for i in os.listdir(path1)]
#filelists=Tcl().call('lsort','-dict',filelists) #comment by xin
filelists.sort(key=natural_key) #add by xin 2026-05-13
T=[]
clustering=[]
value=[]
for file in filelists:
   
    file_list=file.split('_')
    k=[i for i in file_list if i[0]=='k'][0][1:]
    
    graph=file[:-9]+'.txt'
    #print('file',file)
   # print(graph)
    g=load_graph.read_g(path2+graph)
    edge=[]
    p=[]
    for u,v,w in g.edges(data=True):
        edge.append((u,v))
        p.append(w['weight'])

    with bz2.open(path1+file,'rt') as f:
        data=json.load(f)
    # convert the table to dataframe
    #clustering_df=pd.DataFrame(data['tables']['clustering'])
   

    #cluster=Trans_C1(list(clustering_df['clabel']))
    #below add by xin 2026-05-13
    clusters = defaultdict(list)
    for row in data["tables"]["clustering"]:
        #clusters[str(row["center"])].append(int(row["label"])) #comment by xin
        clusters[str(row["clabel"])].append(int(row["label"])) 
    cluster_list = list(clusters.values())
    data_acpc = {
        str(len(cluster_list)): cluster_list
    }
    cluster=list(data_acpc.values())[0]
    acpc_clustering.update({k:cluster})
    #print(cluster)
   
print(acpc_clustering)
  

import json
path='mcp_acp_data//l10_p0.3_evolving_lowP1//result//acpc//'
with open(path+'acpc_increaseK_lowP.json','w') as fp:
          json.dump(acpc_clustering,fp,indent=4) # With indent=4 (pretty format)
print('acpc clustering saved')
'''

#draw Figure 12: expected modularity values under high probability distribution graph
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
from os import listdir
importlib.reload(load_graph)
acpc_clustering={}
path1='mcp_acp_data//l10_p0.3_evolving_highP1//result//acpc//'
path2='mcp_acp_data//l10_p0.3_evolving_highP1//datasets//'
filelists=[i for i in os.listdir(path1)]
#filelists=Tcl().call('lsort','-dict',filelists) #comment by xin
filelists.sort(key=natural_key) #add by xin 2026-05-13
T=[]
clustering=[]
value=[]
for file in filelists:
   
    file_list=file.split('_')
    k=[i for i in file_list if i[0]=='k'][0][1:]
    
    graph=file[:-9]+'.txt'
    print('file',file)
    print(graph)
    g=load_graph.read_g(path2+graph)
    edge=[]
    p=[]
    for u,v,w in g.edges(data=True):
        edge.append((u,v))
        p.append(w['weight'])

    with bz2.open(path1+file,'rt') as f:
        data=json.load(f)
    #clustering_df=pd.DataFrame(data['tables']['clustering'])
   

    #cluster=Trans_C1(list(clustering_df['clabel']))
    #below add by xin 2026-05-13
    clusters = defaultdict(list)
    for row in data["tables"]["clustering"]:
        #clusters[str(row["center"])].append(int(row["label"])) #comment by xin
        clusters[str(row["clabel"])].append(int(row["label"])) 
    cluster_list = list(clusters.values())
    data_acpc = {
        str(len(cluster_list)): cluster_list
    }
    cluster=list(data_acpc.values())[0]
    acpc_clustering.update({k:cluster})
   
   
print(acpc_clustering)

import json
path='mcp_acp_data//l10_p0.3_evolving_highP1//result//acpc//'
with open(path+'acpc_increaseK_highP.json','w') as fp:
          json.dump(acpc_clustering,fp,indent=4) # With indent=4 (pretty format)
'''

# expected modularity in structure-aware/unaware probability distribution graph -RQ5
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

from os import listdir
importlib.reload(load_graph)
acpc_clustering={}
path1='mcp_acp_data//l50_k2_p0.18_polarized_graph//result//acpc//'
path2='mcp_acp_data//l50_k2_p0.18_polarized_graph//datasets//'
filelists=[i for i in os.listdir(path1) if i !='.DS_Store' and i !='acpc_polarized.json']
#filelists=Tcl().call('lsort','-dict',filelists) #comment by xin
filelists.sort(key=natural_key) #add by xin 2026-05-13
T=[]
clustering=[]
value=[]
for file in filelists:
    print(file)
    file_list=file.split('_')
    k=[i for i in file_list if i[0]=='k'][0][1:]
    name=file_list[-2]
    
    graph=file[:-9]+'.txt'
    print('file',file)
    #print(graph)
    g=load_graph.read_g(path2+graph)
    edge=[]
    p=[]
    for u,v,w in g.edges(data=True):
        edge.append((u,v))
        p.append(w['weight'])

    with bz2.open(path1+file,'rt') as f:
        data=json.load(f)
    # convert the table to dataframe
    #clustering_df=pd.DataFrame(data['tables']['clustering'])
   

    #cluster=Trans_C1(list(clustering_df['clabel']))
    #below add by xin 2026-05-13
    clusters = defaultdict(list)
    for row in data["tables"]["clustering"]:
        #clusters[str(row["center"])].append(int(row["label"])) #comment by xin
        clusters[str(row["clabel"])].append(int(row["label"])) 
    cluster_list = list(clusters.values())
    data_acpc = {
        str(len(cluster_list)): cluster_list
    }
    cluster=list(data_acpc.values())[0]
    acpc_clustering.update({name:cluster})
    print(cluster)
    mod=APWP(edge,p,cluster)
    print(file,':',mod)
   
print(acpc_clustering)
'''
import json
path='mcp_acp_data//l50_k2_p0.18_polarized_graph//result//acpc//'
with open(path+'acpc_polarized.json','w') as fp:
          json.dump(acpc_clustering,fp,indent=4) # With indent=4 (pretty format)
'''