# Benchmarking Clustering Methods for Uncertain Networks

## download repo
```
git clone https://github.com/XINS3/Evaluation.git
cd Evaluation
```
## How to reproduce figures in the paper?
  * Figure.5 - Figure.8 run:
    
     ```
    python Experiments_on_real-world_datasets_RQ1.py
     ```
    
  * Figure.9 - Figure.10 run:
    
    ```
    python Experiments_on_Effect_of_Shifting_Probabilities_RQ2.py
    ```
    
  * Figure.11 - Figure.12 run:
    
    ```
    python Experiments_on_Influence_of_Communinity_strength_RQ3.py
    ```
    
  * Figure.13 run:
    
    ```
    python Experiment_on_Influence_of_Number_of_Clusters_RQ4.py
    ```
    
  * Figure 14 & 15 & 17 & 19 (plots) run:
    
    ```
    python Experiment_on_Performances_under_Different_Probability_Distributions_RQ5.py
    ```

## How to reproduce results by algorithms?
  * ACP: test_acpc.ipynb
  * GMM: test_gmm.ipynb
  * Infomap: test_infomap.ipynb
  * MCP: test_mcp_acp.ipynb
  * pKwikCluster: test_pkwik.ipynb
  * Bayes approach: test_structural_inference.ipynb
  * Louvain: test_weightedLouvain.ipynb
