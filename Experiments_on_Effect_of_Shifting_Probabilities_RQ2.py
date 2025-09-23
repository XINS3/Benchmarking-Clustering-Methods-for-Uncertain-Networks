# calculate AMI

import json
from sklearn.metrics.cluster import adjusted_mutual_info_score as ami
from Expected_mod import Trans_C1, Trans_C2, APWP
path='mcp_acp_data//l10_k10_p0.4_multiplied//new//'
k=10
l=10
cc=[i for i in range(k*l)]
    
stad_cluster=[cc[x:x+l] for x in range(0, len(cc), l)]
print(stad_cluster)

# bayes
multi_bayes=[0.0,0.1,0.2,0.3,0.4,0.5]
ami_bayes=[0.0,
0.052110446998558366,
0.14358515197742952,
0.10328452454688823,
0.11058687449591724,
0.09414022196351422]

# mcp
path2='mcp_results//'
with open(path+path2+'mcpc.json','r') as fp:
    data=json.load(fp)
multi_mcp=[]
ami_mcp=[]
mod_mcp=[]
for _ in data:
    multi_mcp.append(float(_))
    ami_mcp.append(ami(Trans_C2(stad_cluster,k*l),Trans_C2(data[str(_)],k*l)))
print(ami_mcp)

#acp

path2='acp_results//'
with open(path+path2+'acpc.json','r') as fp:
    data=json.load(fp)
multi_acp=[]
ami_acp=[]
for _ in data:
    multi_acp.append(float(_))
    ami_acp.append(ami(Trans_C2(stad_cluster,k*l),Trans_C2(data[str(_)],k*l)))
multi_acp

# gmm

path2='gmm_results//'
with open(path+path2+'gmm.json','r') as fp:
    data=json.load(fp)
multi_gmm=[]
ami_gmm=[]
for _ in data:
    multi_gmm.append(float(_))
    ami_gmm.append(ami(Trans_C2(stad_cluster,k*l),Trans_C2(data[str(_)],k*l)))
multi_gmm
   

#louvain

path2='louvain_results//'
with open(path+path2+'louvain.json','r') as fp:
    data=json.load(fp)
multi_louvain=[]
ami_louvain=[]
for _ in data:
    multi_louvain.append(float(_))
    ami_louvain.append(ami(Trans_C2(stad_cluster,k*l),Trans_C2(data[str(_)],k*l)))


#info

path2='Infomap_results//'
with open(path+path2+'infomap.json','r') as fp:
    data=json.load(fp)
multi_info=[]
ami_info=[]
for _ in data:
    multi_info.append(float(_))
    ami_info.append(ami(Trans_C2(stad_cluster,k*l),Trans_C2(data[str(_)],k*l)))

#pkwik

path2='pwik_results//'
with open(path+path2+'pwik.json','r') as fp:
    data=json.load(fp)
multi_pwik=[]
ami_pwik=[]
for _ in data:
    multi_pwik.append(float(_))
    ami_pwik.append(ami(Trans_C2(stad_cluster,k*l),Trans_C2(data[str(_)],k*l)))

#embed

path2='embedding//'
with open(path+path2+'embedding_l10_k10_p0.4_multiplied.json','r') as fp:
    data=json.load(fp)
multi_embed=[]
ami_embed=[]
for _ in data:
    multi_embed.append(float(_))
    ami_embed.append(ami(Trans_C2(stad_cluster,k*l),Trans_C2(data[str(_)],k*l)))

##################################

# draw Figure 9: AMI values with different ranges of edge probabilities.

import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap


data= [ami_mcp,ami_acp,ami_pwik,ami_bayes,ami_embed,ami_louvain,ami_gmm,ami_info]
X= [ multi_mcp,multi_acp,multi_pwik,multi_bayes,multi_embed,multi_louvain,multi_gmm,multi_info]
colors = get_cmap('tab10').colors #colors=['k', 'limegreen', 'saddlebrown', 'royalblue','cyan','tomato','gold','magenta']
markers = ['o', 's', 'D', '^', 'v', '<', '>', 'p', '*']
linestyles = ['--', '--', '-.', ':', '--', '--', '-.', ':', '--']
labels = ['MCP', 'ACP','Pkwikcluster', 'Bayes','URGE','Louvain', 
          'GMM', 'Infomap']

plt.figure(figsize=(10, 6))
for i in range(len(data)):
     
    plt.plot(
        X[i], data[i],
        label=labels[i],
        marker=markers[i],
        markersize=6,                     # Smaller marker
        linestyle=linestyles[i % len(linestyles)],#linestyle='-',                   # Line added
        linewidth=1.2,                   # Visible but clean line
        markerfacecolor=colors[i % len(colors)],
        markeredgewidth=0.5,  
        color=colors[i % len(colors)],
        markeredgecolor='black'  
    )


plt.tight_layout()


plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.5)
plt.minorticks_on() 

plt.legend()
plt.xlabel('Shifting range')
plt.ylabel('AMI')
#plt.savefig('fig//ami_multiplied.pdf',bbox_inches='tight', pad_inches=0.1)

####################################################

# calculate expected modularity

import json
import load_graph
from Expected_mod import APWP

# 读各算法结果（和图无关，只读一次）
path2='mcp_results//'
with open(path+path2+'mcpc.json','r') as fp:
    data_mcp=json.load(fp)

path2='acp_results//'
with open(path+path2+'acpc.json','r') as fp:
    data_acp=json.load(fp)

path2='gmm_results//'
with open(path+path2+'gmm.json','r') as fp:
    data_gmm=json.load(fp)

path2='louvain_results//'
with open(path+path2+'louvain.json','r') as fp:
    data_louvain=json.load(fp)

path2='Infomap_results//'
with open(path+path2+'infomap.json','r') as fp:
    data_info=json.load(fp)

path2='pwik_results//'
with open(path+path2+'pwik.json','r') as fp:
    data_pwik=json.load(fp)

path2='embedding//'
with open(path+path2+'embedding_l10_k10_p0.4_multiplied.json','r') as fp:
    data_embed=json.load(fp)


for i in range(5):
    g = load_graph.read_g(path + f'datasets//k10_l10_p0.4_multi0{i}.txt')
    edge=[]
    P=[]
    for (u,v,p) in g.edges(data=True):
        edge.append((u,v))
        P.append(p['weight'])

    print(f'\n=== k10_l10_p0.4_multi0{i}.txt ===')
    for t in [f'{x/10:.1f}' for x in range(0, 6)]:  # '0.0','0.1',...,'0.5'
        print(f'-- threshold {t} --')
        print('mcp-'+t,     APWP(edge, P, data_mcp[t]))
        print('acp-'+t,     APWP(edge, P, data_acp[t]))
        print('gmm-'+t,     APWP(edge, P, data_gmm[t]))
        print('louvain-'+t, APWP(edge, P, data_louvain[t]))
        print('info-'+t,    APWP(edge, P, data_info[t]))
        print('pwik-'+t,    APWP(edge, P, data_pwik[t]))
        print('embed-'+t,   APWP(edge, P, data_embed[t]))


#########################################

# draw Figure 10: Expected modularity values with different ranges of edge probabili-
ties.

mod_baye=[-9.288864649273505e-05, -0.00027981222043274676, -0.0004015840793799629, -0.00039445824285477723, -0.00039834092173267083, -0.0004118062040204506]
mod_mcp=[-0.0005838009802469737,0.006886465673644421,-0.00471407507279181,-0.0007715534386631739,0.0,0.0]
mod_acp=[-0.002205994473070036,-0.0014570700110550976,0.0018634722423334252,-0.00024043329965680945,0.0,0.0]
mod_gmm=[-0.005724299583617497,-0.011581277341184042,0.00575403365919621,0.020768968019775413,-0.025488262672617636,-0.008534643038367571]
mod_louvain=[0.48928169032440977,0.4932368734171953,0.4944166148136377,0.49619868537861367,0.4971380081776314,0.4978242043071648]
mod_info=[0.4862919942088216,0.4926004972944971,0.4932881587582906,0.493714744891231,0.49459220579731206,0.4947472202311584]
mod_pwik=[-0.01358894713779342,0.12502803750450164,0.1761531049482185,0.16187756717672078,0.22090960932667564,0.2749405992359015]
mod_embed=[0.4236765877932612,0.4448367259047611,0.4649242275623642,0.47939611456374587,0.47924347849574855,0.48560420386614417]


import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap


data= [mod_mcp,mod_acp,mod_pwik,mod_baye,mod_embed,mod_louvain,mod_gmm,mod_info]
X= [ 0.0,0.1,0.2,0.3,0.4,0.5]
colors = get_cmap('tab10').colors #colors=['k', 'limegreen', 'saddlebrown', 'royalblue','cyan','tomato','gold','magenta']
markers = ['o', 's', 'D', '^', 'v', '<', '>', 'p', '*']
linestyles = ['--', '--', '-.', ':', '--', '--', '-.', ':', '--']
labels = ['MCP', 'ACP','Pkwikcluster', 'Bayes','URGE','Louvain', 
          'GMM', 'Infomap']

plt.figure(figsize=(10, 6))
for i in range(len(data)):
     
    plt.plot(
        X, data[i],
        label=labels[i],
        marker=markers[i],
        markersize=6,                     # Smaller marker
        linestyle=linestyles[i % len(linestyles)],#linestyle='-',                   # Line added
        linewidth=1.2,                   # Visible but clean line
        markerfacecolor=colors[i % len(colors)],
        markeredgewidth=0.5,  
        color=colors[i % len(colors)],
        markeredgecolor='black'  
    )

plt.tight_layout()


plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.5)
plt.minorticks_on() 

plt.legend()
plt.xlabel('Shifting range')
plt.ylabel('Expected Modularity')
#plt.savefig('fig//expMod_multiplied.pdf',bbox_inches='tight', pad_inches=0.1)


