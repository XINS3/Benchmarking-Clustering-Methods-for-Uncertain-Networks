# draw Figure 17: Expected modularity values from clustering calculated by different algorithms in a structure-aware probability distribution graph
# structure-aware/unaware json file groups all nodes into single cluster, so the expected modularity is the same as original 2026-05-14
'''
import matplotlib.pyplot as plt

louvain=0.3300113774796969
mcp=0.0
acp=0.0
info=0.3300113774796969
gmm=-0.002393922128711668
gmm_v2=0.02748247410079403
pwikk=0.0641936319907223
embed=0.3300113774796969
bayes=0.08703319429437471


methods = ['MCP', 'ACP','Pkwikcluster','Bayes', 'URGE','Louvain', 'GMM', 'Infomap'  ]
f1_scores=  [mcp, acp,pwikk,bayes,embed,louvain,gmm_v2,info]

hatches = ['/', '\\', 'x', '-', '|', '+', '.', '*']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(methods, f1_scores, width=0.4, color='white', edgecolor='black')

# 设置每根柱子的花纹
for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)

# 添加标签
#plt.title('Expected modularity', fontsize=17, fontweight='bold')
ax.set_xlabel('Method', fontsize=17, fontweight='bold')
ax.set_ylabel('Expected modularity', fontsize=17, fontweight='bold')
ax.set_ylim(min(f1_scores) - 0.05, max(f1_scores) + 0.08)

# add labels only once
ax.bar_label(
    bars,
    fmt='%.3f',
    padding=3,
    fontsize=15
)
# # 添加数值标签
# for i, score in enumerate(f1_scores):
#     ax.text(i, score + 0.02, f"{score:.2f}", ha='center', fontsize=17)

ax.set_xticklabels(methods, rotation=30)  # 方法名倾斜一点，防止重叠

plt.tight_layout()
plt.tick_params(axis='both', labelsize=17)
fig.tight_layout(pad=2.0)


plt.savefig('fig//unorder_exMod_v3.pdf')
plt.show()

###############################################

# draw Figure 19: Expected modularity values from clustering calculated by different algorithms in a structure-unaware probability distribution graph.



import matplotlib.pyplot as plt

louvain=0.05725757090684386
mcp=0.0
acp=0.0
info=0.0
gmm=0.0018789197572546628
gmm_v2=0.01205547309576942
pwikk=0.01195438153058849
embed=0.04775279154669124
bayes=0.024314377802170183


methods = ['MCP', 'ACP','Pkwikcluster','Bayes', 'URGE','Louvain', 'GMM', 'Infomap'  ]
f1_scores=  [mcp, acp,pwikk,bayes,embed,louvain,gmm_v2,info]

hatches = ['/', '\\', 'x', '-', '|', '+', '.', '*']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(methods, f1_scores, width=0.4, color='white', edgecolor='black')

# 设置每根柱子的花纹
for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)

# 添加标签
#plt.title('Expected modularity', fontsize=17, fontweight='bold')
ax.set_xlabel('Method', fontsize=17, fontweight='bold')
ax.set_ylabel('Expected modularity', fontsize=17, fontweight='bold')
ax.set_ylim(min(f1_scores) - 0.05, max(f1_scores) + 0.08)

# add labels only once
ax.bar_label(
    bars,
    fmt='%.3f',
    padding=3,
    fontsize=15
)
# # 添加数值标签
# for i, score in enumerate(f1_scores):
#     ax.text(i, score + 0.02, f"{score:.2f}", ha='center', fontsize=17)

ax.set_xticklabels(methods, rotation=30)  # 方法名倾斜一点，防止重叠

plt.tight_layout()
plt.tick_params(axis='both', labelsize=17)
fig.tight_layout(pad=2.0)


plt.savefig('fig//order_exMod_v3.pdf')
plt.show()

'''
######################################
# draw Figure 11: expected modularity values under low probability distribution graph
'''

import json 
path3='mcp_acp_data//l10_p0.3_evolving_lowP1//result//'
# gmm
path2='gmm//gmm_increaseK_lowP.json'
with open(path3+path2,'r') as fp:
    data=json.load(fp)
print(data['5'])
cluster_gmm=data['5']


#from sklearn.metrics.cluster import adjusted_mutual_info_score as ami
from Expected_mod import Trans_C2, APWP

# graph
path_graph='mcp_acp_data//l10_p0.3_evolving_lowP1//dataset//k5_l10_p0.3.txt'
import load_graph
g=load_graph.read_g(path_graph)
edge=[]
p=[]
for u,v,w in g.edges(data=True):
    edge.append((u,v))
    p.append(w['weight'])
print(APWP(edge,p,cluster_gmm))




import matplotlib.pyplot as plt


gmm=-0.0338
gmm_v2=0.19011111020743157
pwikk=-0.0663
mcp=-0.0128
mcp_v2=0.3185710481020486
info=0.4218
bayes=0.00
acp=0.0112
acp_v2 = 0.2678755529113721
louvain=0.4218
embed=0.3617
#f1_scores = [mcp,louvain,acp,info,gmm,pwikk,embed,bayes]
methods = ['MCP', 'ACP','Pkwikcluster','Bayes', 'URGE','Louvain', 'GMM', 'Infomap'  ]
f1_scores=  [mcp_v2, acp_v2,pwikk,bayes,embed,louvain,gmm_v2,info]
print(f1_scores)

# 8种不同的黑白花纹（可自定义）
hatches = ['/', '\\', 'x', '-', '|', '+', '.', '*']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(methods, f1_scores, width=0.4, color='white', edgecolor='black')

# 设置每根柱子的花纹
for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)

# 添加标签
#plt.title('Expected modularity', fontsize=17, fontweight='bold')
ax.set_xlabel('Method', fontsize=17, fontweight='bold')
ax.set_ylabel('Expected modularity', fontsize=17, fontweight='bold')
ax.set_ylim(min(f1_scores) - 0.05, max(f1_scores) + 0.08)

# add labels only once
ax.bar_label(
    bars,
    fmt='%.3f',
    padding=3,
    fontsize=15
)
# # 添加数值标签
# for i, score in enumerate(f1_scores):
#     ax.text(i, score + 0.02, f"{score:.2f}", ha='center', fontsize=17)

ax.set_xticklabels(methods, rotation=30)  # 方法名倾斜一点，防止重叠

plt.tight_layout()
plt.tick_params(axis='both', labelsize=17)
fig.tight_layout(pad=2.0)
plt.savefig('fig//low_prob_v3.pdf')
plt.show()

'''
###############################
# draw Figure 12: expected modularity values under high probability distribution graph

import json 
path3='mcp_acp_data//l10_p0.3_evolving_highP1//result//'
# gmm
path2='gmm//gmm_increaseK_highP.json'
with open(path3+path2,'r') as fp:
    data=json.load(fp)
print('gmm',data['5'])
cluster_gmm=data['5']






from Expected_mod import Trans_C2, APWP

# graph
path_graph='mcp_acp_data//l10_p0.3_evolving_highP1//datasets//k5_l10_p0.3.txt'
import load_graph
g=load_graph.read_g(path_graph)
edge=[]
p=[]
for u,v,w in g.edges(data=True):
    edge.append((u,v))
    p.append(w['weight'])
print('gmm',APWP(edge,p,cluster_gmm))



'''
import matplotlib.pyplot as plt

# 示例：8个方法与对应F1分数
#methods = ['MCP', 'Louvain', 'ACP', 'Infomap', 'GMM', 'Pkwikcluster', 'URGE', 'Bayes']
gmm=-0.0342
gmm_v2=0.03416750173776495
pwikk=0.2421
mcp=0.000
mcp_v2=0 # add by xin, 2026-05-14
info=0.4998
bayes=0.4224
acp=0.000
acp_v2 = 0 # add by xin, 2026-05-13
louvain=0.4998
embed=0.4902
#f1_scores = [mcp,louvain,acp,info,gmm,pwikk,embed,bayes]
methods = ['MCP', 'ACP','Pkwikcluster','Bayes', 'URGE','Louvain', 'GMM', 'Infomap'  ]
f1_scores=  [mcp_v2, acp_v2,pwikk,bayes,embed,louvain,gmm_v2,info]
print(f1_scores)
# 8种不同的黑白花纹（可自定义）
hatches = ['/', '\\', 'x', '-', '|', '+', '.', '*']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(methods, f1_scores, width=0.4, color='white', edgecolor='black')

# 设置每根柱子的花纹
for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)

# 添加标签
#plt.title('Expected modularity', fontsize=17, fontweight='bold')
ax.set_xlabel('Method', fontsize=17, fontweight='bold')
ax.set_ylabel('Expected modularity', fontsize=17, fontweight='bold')
ax.set_ylim(min(f1_scores) - 0.05, max(f1_scores) + 0.08)

# add labels only once
ax.bar_label(
    bars,
    fmt='%.3f',
    padding=3,
    fontsize=15
)
# # 添加数值标签
# for i, score in enumerate(f1_scores):
#     ax.text(i, score + 0.02, f"{score:.2f}", ha='center', fontsize=17)

ax.set_xticklabels(methods, rotation=30)  # 方法名倾斜一点，防止重叠

plt.tight_layout()
plt.tick_params(axis='both', labelsize=17)
fig.tight_layout(pad=2.0)

plt.savefig('fig//high_prob_v3.pdf')
plt.show()


'''