

import matplotlib.pyplot as plt


gmm=-0.0338
pwikk=-0.0663
mcp=-0.0128
info=0.4218
bayes=0.00
acp=0.0112
louvain=0.4218
embed=0.3617
#f1_scores = [mcp,louvain,acp,info,gmm,pwikk,embed,bayes]
methods = ['MCP', 'ACP','Pkwikcluster','Bayes', 'URGE','Louvain', 'GMM', 'Infomap'  ]
f1_scores=  [mcp, acp,pwikk,bayes,embed,louvain,gmm,info]
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
plt.savefig('fig//low_prob_v2.pdf')
plt.show()
