
import json
def read_clustering(file):
    '''
    Reads a clustering from a file and returns it as a list of sets.
    node id represented as number.
    '''
    import csv
    cluster=[]
    with open (file, 'r' )as f:
        for line in f:
            nodes=line.strip().split()
            cluster.append(set(g.upper().strip() for g in nodes))
    # transform node id to number
    for i in range(len(cluster)):
        
        cluster[i]=set(int(g) for g in cluster[i])
    return cluster
'''
def f1_set(a, b):
    a, b = set(a), set(b)
    if len(a) == 0 and len(b) == 0:
        return 1.0
    if len(a) == 0 or len(b) == 0:
        return 0.0
    inter = len(a & b)
    return 2 * inter / (len(a) + len(b))

def best_match_f1(true_clusters, pred_clusters):
    """
    true_clusters: overlapping allowed
    pred_clusters: non-overlapping or overlapping
    returns directional and combined F1
    """
    true_sets = [set(c) for c in true_clusters if len(c) > 0]
    pred_sets = [set(c) for c in pred_clusters if len(c) > 0]

    if len(true_sets) == 0 or len(pred_sets) == 0:
        return {
            "F_pred": 0.0,
            "F_true": 0.0,
            "F1_overall": 0.0,
        }

    # predicted -> true
    F_pred = sum(max(f1_set(pc, tc) for tc in true_sets) for pc in pred_sets) / len(pred_sets)

    # true -> predicted
    F_true = sum(max(f1_set(tc, pc) for pc in pred_sets) for tc in true_sets) / len(true_sets)

    F1_overall = 2 * F_pred * F_true / (F_pred + F_true) if (F_pred + F_true) > 0 else 0.0

    return {
        "F_pred": F_pred,
        "F_true": F_true,
        "F1_overall": F1_overall,
    }
'''
def complex_match_score(pred_cluster, true_cluster):
    """
    score(P, T) = |P ∩ T|^2 / (|P| * |T|)
    """
    P = set(pred_cluster)
    T = set(true_cluster)

    if len(P) == 0 or len(T) == 0:
        return 0.0

    inter = len(P & T)
    return (inter * inter) / (len(P) * len(T))


def best_match_f1(true_clusters, pred_clusters, thr=0.3):
    """
    true_clusters: list of iterables/sets, overlapping allowed
    pred_clusters: list of iterables/sets, non-overlapping or overlapping both OK
    thr: matching threshold, commonly 0.2 or 0.25

    returns:
        {
            'precision': ...,
            'recall': ...,
            'f1': ...,
            'matched_pred': ...,
            'matched_true': ...,
            'n_pred': ...,
            'n_true': ...
        }
    """
    true_sets = [set(c) for c in true_clusters if len(c) > 0]
    pred_sets = [set(c) for c in pred_clusters if len(c) > 0]

    n_true = len(true_sets)
    n_pred = len(pred_sets)

    if n_true == 0 or n_pred == 0:
        return {
            'precision': 0.0,
            'recall': 0.0,
            'f1': 0.0,
            'matched_pred': 0,
            'matched_true': 0,
            'n_pred': n_pred,
            'n_true': n_true
        }

    # precision side: predicted complexes matched by at least one true complex
    matched_pred = 0
    for P in pred_sets:
        best = max(complex_match_score(P, T) for T in true_sets)
        if best >= thr:
            matched_pred += 1

    # recall side: true complexes matched by at least one predicted complex
    matched_true = 0
    for T in true_sets:
        best = max(complex_match_score(P, T) for P in pred_sets)
        if best >= thr:
            matched_true += 1

    precision = matched_pred / n_pred if n_pred > 0 else 0.0
    recall = matched_true / n_true if n_true > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

    return {
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'matched_pred': matched_pred,
        'matched_true': matched_true,
        'n_pred': n_pred,
        'n_true': n_true
    }
#pathground='mcp_acp_data//krogan2006_core//intersec_mips//ground_truth//krogan2006_core_mips_clustering.txt'
pathground='mcp_acp_data//krogan2006_extended//intersec_mips//ground_truth//krogan2006_extended_mips_clustering.txt'


truth_cluster=read_clustering(pathground)
#print(type(truth_cluster))
#print(truth_cluster)

#path='mcp_acp_data//krogan2006_core//intersec_mips//'
path = 'mcp_acp_data//krogan2006_extended//intersec_mips//'
path_mcpc='mcpc_results'
pacpc='acpc_results'
pgmm='gmm_results'
plouvain='louvain_results'
pinfo='Infomap_results'
ppwik='pwik_results'
pbaye='baye_results'
pembedding='embedding_results'

#with open(path+pacpc+'//acpc_k188.json','r') as fp: #core
with open(path+pacpc+'//acpc_k195.json','r') as fp: #extended
    data_acpc=json.load(fp)
pre_acpc=list(data_acpc.values())[0]
#print(pre_acpc)
f1_acpc=best_match_f1(truth_cluster,pre_acpc)
print('acpc F1:',f1_acpc)
#with open(path+path_mcpc+'//mcpc_k188.json','r') as fp:#core
with open(path+path_mcpc+'//mcpc_k195.json','r') as fp:#extended
    data_mcpc=json.load(fp)
pre_mcpc=list(data_mcpc.values())[0]
f1_mcpc=best_match_f1(truth_cluster,pre_mcpc)
print('mcpc F1:',f1_mcpc)
#with open(path+pgmm+'//gmm_k188.json','r') as fp:#core
with open(path+pgmm+'//gmm_k195.json','r') as fp:#extended
    data_gmm=json.load(fp)
pre_gmm=list(data_gmm.values())[0]
f1_gmm=best_match_f1(truth_cluster,pre_gmm)
print('gmm F1:',f1_gmm)
with open(path+plouvain+'//louvain.json','r') as fp:
    data_louvain=json.load(fp)
pre_louvain=list(data_louvain.values())[0]
f1_louvain=best_match_f1(truth_cluster,pre_louvain)
print('louvain F1:',f1_louvain)
#with open(path+pinfo+'//infomap.json','r') as fp: #core
with open(path+pinfo+'//infomap.json','r') as fp: #extended
    data_Infomap=json.load(fp)
pre_Infomap=list(data_Infomap.values())[0]
f1_Infomap=best_match_f1(truth_cluster,pre_Infomap)
print('Infomap F1:',f1_Infomap)
#with open(path+ppwik+'//pwik5.json','r') as fp:#core
with open(path+ppwik+'//pwik.json','r') as fp:#extended
    data_pwik=json.load(fp)
pre_pwik=list(data_pwik.values())[0]


f1_pwik=best_match_f1(truth_cluster,pre_pwik)
print('pwik F1:',f1_pwik)
#with open(path+pbaye+'//bayes1.json','r') as fp:#core
with open(path+pbaye+'//bayes.json','r') as fp:#extended
    data_baye=json.load(fp)
pre_baye=list(data_baye.values())[0]
f1_baye=best_match_f1(truth_cluster,pre_baye)
print('bayes F1:',f1_baye)
with open(path+pembedding+'//embedding.json','r') as fp:
    data_embedding=json.load(fp)

pre_embedding=list(data_embedding.values())[0]
f1_urge=best_match_f1(truth_cluster,pre_embedding)
print('URGE F1:',f1_urge)
#/mimer/NOBACKUP/groups/naiss2026-4-469/Evaluation/mcp_acp_data/krogan2006_extended/intersec_mips/embedding_results/embedding.json

