import json
import csv
from pathlib import Path
from collections import defaultdict
import statistics

import bz2


def read_clustering(file):
    """
    Reads a ground-truth clustering from a file and returns it as a list of sets.
    Each line is one cluster.
    Node ids are converted to int.
    """
    cluster = []

    with open(file, "r") as f:
        for line in f:
            nodes = line.strip().split()
            if not nodes:
                continue
            cluster.append(set(int(g.upper().strip()) for g in nodes))

    return cluster


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
    true_clusters: list of sets
    pred_clusters: list of sets/lists
    thr: matching threshold

    returns:
        precision, recall, f1, matched_pred, matched_true, n_pred, n_true
    """
    true_sets = [set(c) for c in true_clusters if len(c) > 0]
    pred_sets = [set(c) for c in pred_clusters if len(c) > 0]

    n_true = len(true_sets)
    n_pred = len(pred_sets)

    if n_true == 0 or n_pred == 0:
        return {
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0,
            "matched_pred": 0,
            "matched_true": 0,
            "n_pred": n_pred,
            "n_true": n_true,
        }

    matched_pred = 0
    for P in pred_sets:
        best = max(complex_match_score(P, T) for T in true_sets)
        if best >= thr:
            matched_pred += 1

    matched_true = 0
    for T in true_sets:
        best = max(complex_match_score(P, T) for P in pred_sets)
        if best >= thr:
            matched_true += 1

    precision = matched_pred / n_pred if n_pred > 0 else 0.0
    recall = matched_true / n_true if n_true > 0 else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall) > 0
        else 0.0
    )

    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "matched_pred": matched_pred,
        "matched_true": matched_true,
        "n_pred": n_pred,
        "n_true": n_true,
    }


def json_to_pred_clusters(json_file):
    """
    Reads one ugraph JSON result file and converts it to predicted clusters.

    Expected JSON structure:
        data["tables"]["clustering"]

    Each row should contain:
        row["center"]
        row["label"]
    """
    if json_file.name.endswith(".bz2"):
        opener = bz2.open
        mode = "rt"
    else:
        opener = open
        mode = "r"

    with opener(json_file, mode) as fp:
        data = json.load(fp)

    clusters = defaultdict(list)

    for row in data["tables"]["clustering"]:
        clusters[str(row["center"])].append(int(row["label"]))


    clusters = defaultdict(list)

    for row in data["tables"]["clustering"]:
        center = str(row["center"])
        label = int(row["label"])
        clusters[center].append(label)

    cluster_list = list(clusters.values())
    return cluster_list

from pathlib import Path


def main():
    # 修改这里：ground truth 文件路径
    pathground = (
        "mcp_acp_data/krogan2006_core/intersec_mips/"
        "ground_truth/krogan2006_core_mips_clustering.txt"
    )

    # 修改这里：你的 result 文件夹路径
    result_dir = Path(
        "mcp_acp_data/krogan2006_core/hyperparameter_result" # core, mcpc method.
    )
   
    # 输出 summary csv
    #output_csv = result_dir / "fmeasure_summary.csv"

    # threshold
    threshold = 0.3

    truth_cluster = read_clustering(pathground)

    json_files = sorted(
        result_dir.glob("*.json.bz2"),
        key=lambda p: int(p.stem) if p.stem.isdigit() else p.stem
    )

    if not json_files:
        print(f"No JSON files found in: {result_dir}")
        return

    results = []
    f1_values = []

    for json_file in json_files:
        print(f"Processing: {json_file.name}")
        try:
            pred_cluster = json_to_pred_clusters(json_file)
            score = best_match_f1(
                truth_cluster,
                pred_cluster,
                thr=threshold
            )

            f1 = score["f1"]
            f1_values.append(f1)

       

        except Exception as e:
            print(f"Error processing {json_file.name}: {e}")

    if not f1_values:
        print("No valid F1 values computed.")
        return

    mean_f1 = statistics.mean(f1_values)

    # population variance
    variance_f1 = statistics.pvariance(f1_values)

    
    print()
    print("========== Summary ==========")
    print(f"Number of valid JSON files: {len(f1_values)}")
    print(f"Mean F1: {mean_f1:.6f}")
    print(f"Population variance F1: {variance_f1:.6f}")
    print(f"Sample variance F1: {sample_variance_f1:.6f}")

if __name__ == "__main__":    main()