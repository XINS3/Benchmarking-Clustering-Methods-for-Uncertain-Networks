from Expected_mod import Trans_C1, APWP
import Expected_mod as ex 
import load_graph
import importlib
import pandas as pd 
import json
import bz2
import json
from collections import defaultdict

from Expected_mod import Trans_C1, Trans_C2
from sklearn.metrics.cluster import pair_confusion_matrix
importlib.reload(load_graph)

def f_socre(m):
    tn=m[0][0]
    fn=m[1][0]
    tp=m[1][1]
    fp=m[0][1]
    return 2*tp/(2*tp+fp+fn)

importlib.reload(load_graph)
gmm_clustering={}
path1='mcp_acp_data//krogan2006_core//intersec_mips//gmm_results//'
path2='mcp_acp_data//krogan2006_core//intersec_mips//net//krogan2006_core_mips_net.txt'

T=[]
clustering=[]
value=[]


g=load_graph.read_g(path2)
file1='krogan2006_core_mips_net.json.bz2'

'''
below is the original part of how to transform the json file to the format of clustering

'''
with bz2.open(path1+file1,'rt') as f:
    data=json.load(f)
# convert the table to dataframe
clustering_df=pd.DataFrame(data['tables']['clustering'])
#cluster=Trans_C1(list(clustering_df['clabel'])) # comment by xin
#k=len(cluster) #comment by xin
pre_gmm_v1 = list(clustering_df['clabel']) #add by xin
'''
below is new adding to check Trans_C1
'''
#gmm_clustering.update({k:cluster})
clusters = defaultdict(list)
for row in data["tables"]["clustering"]:
    #clusters[str(row["center"])].append(int(row["label"])) #comment by xin
    clusters[str(row["center"])].append(int(row["id"])) #add by xin
cluster_list = list(clusters.values())
data_gmm = {
    str(len(cluster_list)): cluster_list
}
#--
#cluster=Trans_C1(list(clustering_df['clabel']))
#mcpc_clustering.update({k:cluster})
pre_gmm_v2=list(data_gmm.values())[0]

#print(pre_gmm)

# ground truth clustering

def read_clustering(file):
    import csv
    cluster=[]
    with open (file, 'r' )as f:
        for line in f:
            nodes=line.strip().split()
            cluster.append(set(g.upper().strip() for g in nodes))
    return cluster

pathground='mcp_acp_data//krogan2006_core//intersec_mips//ground_truth//krogan2006_core_mips_clustering.txt'

truth_cluster=read_clustering(pathground)
truth_cluster
true_cluster=[]
for i in truth_cluster:
    
    t=[]
    for j in i:
        
        t.append(int(j))
    true_cluster.append(t)

n=679 # number of nodes after mips

#true_clustercore=Trans_C2(true_cluster,n) # comment by xin

'''
above is original'''

'''
check two way to transform the json file to the format of clustering, and they are the same
'''

print(pre_gmm_v2)
print('------')
# label list to node list
pre_gmm_v1 = Trans_C1(pre_gmm_v1)
pre_gmm_v1.sort()
#print(pre_gmm_v1)
print(pre_gmm_v1==pre_gmm_v2)
print(len(Trans_C1(pre_gmm_v1)),len(pre_gmm_v2))

m=pair_confusion_matrix(true_cluster,pre_gmm)
gmm=f_socre(m)
print('gmm',gmm)