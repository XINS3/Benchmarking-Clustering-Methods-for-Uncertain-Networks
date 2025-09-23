# krogan2006 core

# core network ground truth

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
    
    t=set()
    for j in i:
        
        t.add(int(j))
    true_cluster.append(t)

# read running results

import json
from sklearn.metrics.cluster import pair_confusion_matrix
from sklearn.metrics.cluster import adjusted_mutual_info_score as ami 
from Expected_mod import Trans_C1, Trans_C2
path='mcp_acp_data//krogan2006_core//intersec_mips//'
path_mcpc='mcpc_results'
pacpc='acpc_results'
pgmm='gmm_results'
plouvain='louvain_results'
pinfo='Infomap_results'
ppwik='pwik_results'
pbaye='baye_results'
pembedding='emdedding_results'

n=679 # number of nodes after mips

true_clustercore=Trans_C2(true_cluster,n)
print(true_cluster)
print(len(true_clustercore))
def f_socre(m):
    tn=m[0][0]
    fn=m[1][0]
    tp=m[1][1]
    fp=m[0][1]
    return 2*tp/(2*tp+fp+fn)
with open(path+path_mcpc+'//mcpc_k188.json','r') as fp:
    data_mcpc=json.load(fp)
pre_mcpc=list(data_mcpc.values())[0]
print(len(pre_mcpc))

pre_mcpc2=Trans_C2(pre_mcpc,n)
m=pair_confusion_matrix(true_clustercore,pre_mcpc2)
mcp=f_socre(m)
print('mcp',mcp)

with open(path+pacpc+'//acpc_k188.json','r') as fp:
    data_acpc=json.load(fp)
pre_acpc=list(data_acpc.values())[0]
print(len(pre_acpc))

pre_acpc2=Trans_C2(pre_acpc,n)
m=pair_confusion_matrix(true_clustercore,pre_acpc2)
acp=f_socre(m)
print('acp',acp)

with open(path+pgmm+'//gmm_k188.json','r') as fp:
    data_gmm=json.load(fp)
pre_gmm=list(data_gmm.values())[0]
print(len(pre_gmm))

pre_gmm2=Trans_C2(pre_gmm,n)
m=pair_confusion_matrix(true_clustercore,pre_gmm2)
gmm=f_socre(m)
print('gmm',gmm)

with open(path+plouvain+'//louvain.json','r') as fp:
    data_louvain=json.load(fp)
pre_louvain=list(data_louvain.values())[0]
print(len(pre_louvain))
pre_louvain2=Trans_C2(pre_louvain,n)
m=pair_confusion_matrix(true_clustercore,pre_louvain2)
louvain=f_socre(m)
print('louvain',louvain)

with open(path+pinfo+'//Infomap.json','r') as fp:
    data_Infomap=json.load(fp)
pre_Infomap=list(data_Infomap.values())[0]
print(len(pre_Infomap))


pre_info2=Trans_C2(pre_Infomap,n)
m=pair_confusion_matrix(true_clustercore,pre_info2)
info=f_socre(m)
print('info',info)

with open(path+ppwik+'//pwik2.json','r') as fp:
    data_pwik=json.load(fp)
pre_pwik=list(data_pwik.values())[0]
print(len(pre_pwik))

pre_pwik2=Trans_C2(pre_pwik,n)
m=pair_confusion_matrix(true_clustercore,pre_pwik2)
pwikk=f_socre(m)
print('pwik',pwikk)


with open(path+pbaye+'//bayes1.json','r') as fp:
    data_baye=json.load(fp)
pre_baye=list(data_baye.values())[0]
print(len(pre_baye))

pre_bayes2=Trans_C2(pre_baye,n)
m=pair_confusion_matrix(true_clustercore,pre_bayes2)
bayes=f_socre(m)
print('baye',bayes)

with open(path+pembedding+'//embedding.json','r') as fp:
    data_embedding=json.load(fp)
print(data_embedding)
pre_embedding=list(data_embedding.values())[0]
print(len(pre_embedding))

pre_embedding2=Trans_C2(pre_embedding,n)
m=pair_confusion_matrix(true_clustercore,pre_embedding2)
embed=f_socre(m)
print('embedding',embed)


# draw F1-score:Fig.5 F1-score of krogan2005 core network

import matplotlib.pyplot as plt
mcp= 0.033826576773779295

acp= 0.03346235142331659

gmm= 0.026133115557370357

louvain= 0.34671973843201365

info= 0.15352743561030235

pwikk =0.2772025431425976

bayes= 0.13869226154769046

embed =0.27867698803659396


methods = ['MCP', 'ACP','Pkwikcluster','Bayes', 'URGE','Louvain', 'GMM', 'Infomap'  ]
f1_scores=  [mcp, acp,pwikk,bayes,embed,louvain,gmm,info]

hatches = ['/', '\\', 'x', '-', '|', '+', '.', '*']

plt.figure(figsize=(10, 6))
bars = plt.bar(methods, f1_scores, width=0.4, color='white', edgecolor='black')


for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)



plt.title('F1 Scores', fontsize=14)
plt.xlabel('Method')
plt.ylabel('F1 Score')
plt.ylim(0, 1)


for i, score in enumerate(f1_scores):
    plt.text(i, score + 0.02, f"{score:.2f}", ha='center', fontsize=10)

plt.xticks(rotation=30)  

plt.tight_layout()

#plt.savefig('fig//f1_core.pdf')
plt.show()

#################################################
# AMI calculation

import json
from sklearn.metrics.cluster import pair_confusion_matrix
from sklearn.metrics.cluster import adjusted_mutual_info_score as ami 
path='mcp_acp_data//krogan2006_core//intersec_mips//'
path_mcpc='mcpc_results'
pacpc='acpc_results'
pgmm='gmm_results'
plouvain='louvain_results'
pinfo='Infomap_results'
ppwik='pwik_results'
pbaye='baye_results'
pembedding='emdedding_results'

n=680
print(true_cluster)
true_clustercore=Trans_C2(true_cluster,n)
def f_socre(m):
    tn=m[0][0]
    fn=m[1][0]
    tp=m[1][1]
    fp=m[0][1]
    return 2*tp/(2*tp+fp+fn)
with open(path+path_mcpc+'//mcpc_k188.json','r') as fp:
    data_mcpc=json.load(fp)
pre_mcpc=list(data_mcpc.values())[0]
print(len(pre_mcpc))

pre_mcpc2=Trans_C2(pre_mcpc,n)
mcp=ami(true_clustercore,pre_mcpc2)
print('mcp',mcp)

with open(path+pacpc+'//acpc_k188.json','r') as fp:
    data_acpc=json.load(fp)
pre_acpc=list(data_acpc.values())[0]
print(len(pre_acpc))

pre_acpc2=Trans_C2(pre_acpc,n)
#m=pair_confusion_matrix(true_clustercore,pre_acpc2)
acp=ami(true_clustercore,pre_acpc2)
print('acp',acp)

with open(path+pgmm+'//gmm_k188.json','r') as fp:
    data_gmm=json.load(fp)
pre_gmm=list(data_gmm.values())[0]
print(len(pre_gmm))

pre_gmm2=Trans_C2(pre_gmm,n)
m=pair_confusion_matrix(true_clustercore,pre_gmm2)
gmm=ami(true_clustercore,pre_gmm2)
print('gmm',gmm)

with open(path+plouvain+'//louvain.json','r') as fp:
    data_louvain=json.load(fp)
pre_louvain=list(data_louvain.values())[0]
print(len(pre_louvain))
pre_louvain2=Trans_C2(pre_louvain,n)
m=pair_confusion_matrix(true_clustercore,pre_louvain2)
louvain=ami(true_clustercore,pre_louvain2)
print('louvain',louvain)

with open(path+pinfo+'//Infomap.json','r') as fp:
    data_Infomap=json.load(fp)
pre_Infomap=list(data_Infomap.values())[0]
print(len(pre_Infomap))

pre_info2=Trans_C2(pre_Infomap,n)
m=pair_confusion_matrix(true_clustercore,pre_info2)
info=ami(true_clustercore,pre_info2)
print('info',info)


with open(path+ppwik+'//pwik2.json','r') as fp:
    data_pwik=json.load(fp)
pre_pwik=list(data_pwik.values())[0]
print(len(pre_pwik))

pre_pwik2=Trans_C2(pre_pwik,n)
m=pair_confusion_matrix(true_clustercore,pre_pwik2)
pwikk=ami(true_clustercore,pre_pwik2)
print('pwik',pwikk)


with open(path+pbaye+'//bayes1.json','r') as fp:
    data_baye=json.load(fp)
pre_baye=list(data_baye.values())[0]
print(len(pre_baye))

pre_bayes2=Trans_C2(pre_baye,n)
m=pair_confusion_matrix(true_clustercore,pre_bayes2)
bayes=ami(true_clustercore,pre_bayes2)
print('baye',bayes)




with open(path+pembedding+'//embedding.json','r') as fp:
    data_embedding=json.load(fp)
print(data_embedding)
pre_embedding=list(data_embedding.values())[0]
print(len(pre_embedding))

pre_embedding2=Trans_C2(pre_embedding,n)
m=pair_confusion_matrix(true_clustercore,pre_embedding2)
embed=ami(true_clustercore,pre_embedding2)
print('embedding',embed)


######################################
#draw AMI score:Fig.6 AMI score of krogan2005 core network

import matplotlib.pyplot as plt
mcp= -0.003298297483546002

acp= -0.005410343937751788

gmm= -0.0025833071773839937

louvain= 0.577548301446077

info= 0.4412326464466709

pwikk= 0.47716272500536333

bayes= 0.41938518523615076

embed=0.47315654719654293

methods = ['MCP', 'ACP','Pkwikcluster','Bayes', 'URGE','Louvain', 'GMM', 'Infomap'  ]
ami=  [mcp, acp,pwikk,bayes,embed,louvain,gmm,info]
print(ami)

hatches = ['/', '\\', 'x', '-', '|', '+', '.', '*']

plt.figure(figsize=(10, 6))
bars = plt.bar(methods, ami, width=0.4, color='white', edgecolor='black')

for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)

plt.title('AMI', fontsize=14)
plt.xlabel('Method')
plt.ylabel('AMI')
plt.ylim(-0.1, 1)

for i, score in enumerate(ami):
    plt.text(i, score + 0.02, f"{score:.2f}", ha='center', fontsize=10)

plt.xticks(rotation=30) 

plt.tight_layout()

#plt.savefig('fig//ami_core.pdf')
plt.show()

#####################################################

# krogan2005 extend network

# get ground truth
pathground2='mcp_acp_data//krogan2006_extended//intersec_mips//ground_truth//krogan2006_extended_mips_clustering.txt'
truth_cluster2=read_clustering(pathground2)
truth_cluster
true_cluster2=[]
for i in truth_cluster2:
    
    t=set()
    for j in i:
        
        t.add(int(j))
    true_cluster2.append(t)
print(true_cluster2)

# calculate F1 score
import json
from sklearn.metrics.cluster import pair_confusion_matrix
from sklearn.metrics.cluster import adjusted_mutual_info_score as ami 
path='mcp_acp_data//krogan2006_extended//intersec_mips//'
path_mcpc='mcpc_results'
pacpc='acpc_results'
pgmm='gmm_results'
plouvain='louvain_results'
pinfo='Infomap_results'
ppwik='pwik_results'
pbaye='baye_results'
pembedding='embedding_results'

true_clustercore=Trans_C2(true_cluster2,794)
n=794
def f_socre(m):
    tn=m[0][0]
    fn=m[1][0]
    tp=m[1][1]
    fp=m[0][1]
    return 2*tp/(2*tp+fp+fn)
with open(path+path_mcpc+'//mcpc_k195.json','r') as fp:
    data_mcpc=json.load(fp)
pre_mcpc=list(data_mcpc.values())[0]
print(len(pre_mcpc))

pre_mcpc2=Trans_C2(pre_mcpc,n)
m=pair_confusion_matrix(true_clustercore,pre_mcpc2)
mcp=f_socre(m)
print('mcp',mcp)

with open(path+pacpc+'//acpc_k195.json','r') as fp:
    data_acpc=json.load(fp)
pre_acpc=list(data_acpc.values())[0]
print(len(pre_acpc))

pre_acpc2=Trans_C2(pre_acpc,n)
m=pair_confusion_matrix(true_clustercore,pre_acpc2)
acp=f_socre(m)
print('acp',acp)

with open(path+pgmm+'//gmm_k195.json','r') as fp:
    data_gmm=json.load(fp)
pre_gmm=list(data_gmm.values())[0]
print(len(pre_gmm))

pre_gmm2=Trans_C2(pre_gmm,n)
m=pair_confusion_matrix(true_clustercore,pre_gmm2)
gmm=f_socre(m)
print('gmm',gmm)

with open(path+plouvain+'//louvain.json','r') as fp:
    data_louvain=json.load(fp)
pre_louvain=list(data_louvain.values())[0]
print(len(pre_louvain))
pre_louvain2=Trans_C2(pre_louvain,n)
m=pair_confusion_matrix(true_clustercore,pre_louvain2)
louvain=f_socre(m)
print('louvain',louvain)

with open(path+pinfo+'//Infomap.json','r') as fp:
    data_Infomap=json.load(fp)
pre_Infomap=list(data_Infomap.values())[0]
print(len(pre_Infomap))

pre_info2=Trans_C2(pre_Infomap,n)
m=pair_confusion_matrix(true_clustercore,pre_info2)
info=f_socre(m)
print('info',info)


with open(path+ppwik+'//pwik.json','r') as fp:
    data_pwik=json.load(fp)
pre_pwik=list(data_pwik.values())[0]
print(len(pre_pwik))

pre_pwik2=Trans_C2(pre_pwik,n)
m=pair_confusion_matrix(true_clustercore,pre_pwik2)
pwikk=f_socre(m)
print('pwik',pwikk)


with open(path+pbaye+'//bayes.json','r') as fp:
    data_baye=json.load(fp)
pre_baye=list(data_baye.values())[0]
print(len(pre_baye))

pre_bayes2=Trans_C2(pre_baye,n)
m=pair_confusion_matrix(true_clustercore,pre_bayes2)
bayes=f_socre(m)
print('baye',bayes)

with open(path+pembedding+'//embedding.json','r') as fp:
    data_embedding=json.load(fp)
print(data_embedding)
pre_embedding=list(data_embedding.values())[0]
print(len(pre_embedding))

pre_embedding2=Trans_C2(pre_embedding,n)
m=pair_confusion_matrix(true_clustercore,pre_embedding2)
embed=f_socre(m)
print('embedding',embed)

#########################################

# draw figure 7: F1-score of clustering algorithms in krogan2006 extended network

import matplotlib.pyplot as plt
mcp=0.03489983621015497
louvain=0.2569218598927661
acp=0.035299692016109926
info=0.04545412873474702
gmm=0.02843450479233227
pwikk=0.22907861369399832
embed=0.24465770953294946
bayes=0.10352565885865836

methods = ['MCP', 'ACP','Pkwikcluster','Bayes', 'URGE','Louvain', 'GMM', 'Infomap'  ]
f1_scores=  [mcp, acp,pwikk,bayes,embed,louvain,gmm,info]

hatches = ['/', '\\', 'x', '-', '|', '+', '.', '*']

plt.figure(figsize=(10, 6))
bars = plt.bar(methods, f1_scores, width=0.4, color='white', edgecolor='black')

for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)

plt.title('F1 Scores', fontsize=14)
plt.xlabel('Method')
plt.ylabel('F1 Score')
plt.ylim(0, 1)

for i, score in enumerate(f1_scores):
    plt.text(i, score + 0.02, f"{score:.2f}", ha='center', fontsize=10)

plt.xticks(rotation=30) 

plt.tight_layout()

#plt.savefig('fig//f1_extended.pdf')
plt.show()

#########################################

# calculate AMI

import json
from sklearn.metrics.cluster import pair_confusion_matrix
from sklearn.metrics.cluster import adjusted_mutual_info_score as ami 
from Expected_mod import Trans_C2
path='mcp_acp_data//krogan2006_extended//intersec_mips//'
path_mcpc='mcpc_results'
pacpc='acpc_results'
pgmm='gmm_results'
plouvain='louvain_results'
pinfo='Infomap_results'
ppwik='pwik_results'
pbaye='baye_results'
pembedding='embedding_results'


true_clustercore=Trans_C2(true_cluster2,794)
n=794
def f_socre(m):
    tn=m[0][0]
    fn=m[1][0]
    tp=m[1][1]
    fp=m[0][1]
    return 2*tp/(2*tp+fp+fn)
with open(path+path_mcpc+'//mcpc_k195.json','r') as fp:
    data_mcpc=json.load(fp)
pre_mcpc=list(data_mcpc.values())[0]
print(len(pre_mcpc))

pre_mcpc2=Trans_C2(pre_mcpc,n)
m=pair_confusion_matrix(true_clustercore,pre_mcpc2)
print(true_clustercore)
print(pre_mcpc2)
mcp=ami(true_clustercore,pre_mcpc2)
print('mcp',mcp)

with open(path+pacpc+'//acpc_k195.json','r') as fp:
    data_acpc=json.load(fp)
pre_acpc=list(data_acpc.values())[0]
print(len(pre_acpc))

pre_acpc2=Trans_C2(pre_acpc,n)
m=pair_confusion_matrix(true_clustercore,pre_acpc2)
acp=ami(true_clustercore,pre_acpc2)
print('acp',acp)

with open(path+pgmm+'//gmm_k195.json','r') as fp:
    data_gmm=json.load(fp)
pre_gmm=list(data_gmm.values())[0]
print(len(pre_gmm))

pre_gmm2=Trans_C2(pre_gmm,n)
m=pair_confusion_matrix(true_clustercore,pre_gmm2)
gmm=ami(true_clustercore,pre_gmm2)
print('gmm',gmm)

with open(path+plouvain+'//louvain.json','r') as fp:
    data_louvain=json.load(fp)
pre_louvain=list(data_louvain.values())[0]
print(len(pre_louvain))
pre_louvain2=Trans_C2(pre_louvain,n)
m=pair_confusion_matrix(true_clustercore,pre_louvain2)
louvain=ami(true_clustercore,pre_louvain2)
print('louvain',louvain)

with open(path+pinfo+'//Infomap.json','r') as fp:
    data_Infomap=json.load(fp)
pre_Infomap=list(data_Infomap.values())[0]
print(len(pre_Infomap))

pre_info2=Trans_C2(pre_Infomap,n)
m=pair_confusion_matrix(true_clustercore,pre_info2)
info=ami(true_clustercore,pre_info2)
print('info',info)


with open(path+ppwik+'//pwik.json','r') as fp:
    data_pwik=json.load(fp)
pre_pwik=list(data_pwik.values())[0]
print(len(pre_pwik))

pre_pwik2=Trans_C2(pre_pwik,n)
m=pair_confusion_matrix(true_clustercore,pre_pwik2)
pwikk=ami(true_clustercore,pre_pwik2)
print('pwik',pwikk)


with open(path+pbaye+'//bayes.json','r') as fp:
    data_baye=json.load(fp)
pre_baye=list(data_baye.values())[0]
print(len(pre_baye))

pre_bayes2=Trans_C2(pre_baye,n)
m=pair_confusion_matrix(true_clustercore,pre_bayes2)
bayes=ami(true_clustercore,pre_bayes2)
print('baye',bayes)

with open(path+pembedding+'//embedding.json','r') as fp:
    data_embedding=json.load(fp)
print(data_embedding)
pre_embedding=list(data_embedding.values())[0]
print(len(pre_embedding))

pre_embedding2=Trans_C2(pre_embedding,n)
m=pair_confusion_matrix(true_clustercore,pre_embedding2)
embed=ami(true_clustercore,pre_embedding2)
print('embedding',embed)

############################

# Figure 8: AMI of clustering algorithms in krogan2006 extend network


import matplotlib.pyplot as plt
mcp= -0.009091589102969054

acp= -0.007108447644430976

gmm= -0.019350192650967213

louvain= 0.4796333468630043

info= 0.1309270216635855

pwikk= 0.4224416295549298

bayes= 0.3215756361595477

embed= 0.43360998278704305

methods = ['MCP', 'ACP','Pkwikcluster','Bayes', 'URGE','Louvain', 'GMM', 'Infomap'  ]
ami=  [mcp, acp,pwikk,bayes,embed,louvain,gmm,info]
print(ami)

hatches = ['/', '\\', 'x', '-', '|', '+', '.', '*']

plt.figure(figsize=(10, 6))
bars = plt.bar(methods, ami, width=0.4, color='white', edgecolor='black')


for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)

plt.title('AMI', fontsize=14)
plt.xlabel('Method')
plt.ylabel('AMI')
plt.ylim(-0.1, 1)

for i, score in enumerate(ami):
    plt.text(i, score + 0.02, f"{score:.2f}", ha='center', fontsize=10)

plt.xticks(rotation=30) 
plt.tight_layout()

#plt.savefig('fig//ami_extended.pdf')
plt.show()


