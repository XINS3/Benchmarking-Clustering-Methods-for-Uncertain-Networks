# draw Figure 17: Expected modularity values from clustering calculated by different algorithms in a structure-aware probability distribution graph

import matplotlib.pyplot as plt

louvain=0.3300113774796969
mcp=0.0
acp=0.0
info=0.3300113774796969
gmm=-0.002393922128711668
pwikk=0.0641936319907223
embed=0.3300113774796969
bayes=0.08703319429437471


methods = ['MCP', 'ACP','Pkwikcluster','Bayes', 'URGE','Louvain', 'GMM', 'Infomap'  ]
f1_scores=  [mcp, acp,pwikk,bayes,embed,louvain,gmm,info]

hatches = ['/', '\\', 'x', '-', '|', '+', '.', '*']

plt.figure(figsize=(10, 6))
bars = plt.bar(methods, f1_scores, width=0.4, color='white', edgecolor='black')


for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)


plt.title('Expected modularity', fontsize=14)
plt.xlabel('Method')
plt.ylabel('Expected modularity')
plt.ylim(0, 1)


for i, score in enumerate(f1_scores):
    plt.text(i, score + 0.02, f"{score:.2f}", ha='center', fontsize=10)

plt.xticks(rotation=30)  

plt.tight_layout()

#plt.savefig('fig//unorder_exMod.pdf')
plt.show()

###############################################

# draw Figure 19: Expected modularity values from clustering calculated by different algorithms in a structure-unaware probability distribution graph.



import matplotlib.pyplot as plt

louvain=0.05725757090684386
mcp=0.0
acp=0.0
info=0.0
gmm=0.0018789197572546628
pwikk=0.01195438153058849
embed=0.04775279154669124
bayes=0.024314377802170183


methods = ['MCP', 'ACP','Pkwikcluster','Bayes', 'URGE','Louvain', 'GMM', 'Infomap'  ]
f1_scores=  [mcp, acp,pwikk,bayes,embed,louvain,gmm,info]

hatches = ['/', '\\', 'x', '-', '|', '+', '.', '*']

plt.figure(figsize=(10, 6))
bars = plt.bar(methods, f1_scores, width=0.4, color='white', edgecolor='black')

for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)

plt.title('Expected modularity', fontsize=14)
plt.xlabel('Method')
plt.ylabel('Expected modularity')
plt.ylim(0, 1)

for i, score in enumerate(f1_scores):
    plt.text(i, score + 0.02, f"{score:.2f}", ha='center', fontsize=10)

plt.xticks(rotation=30)  

plt.tight_layout()

# plt.savefig('fig//order_exMod.pdf')
plt.show()
