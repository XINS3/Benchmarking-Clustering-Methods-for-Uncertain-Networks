

def clustering(g,property_map):
    import random as rd 
    import graph_tool.all as gt 
    #q = g.new_ep("double", .98)   # edge uncertainties
    N = g.num_vertices()
    E = g.num_edges()
    #e = g.edge(11, 36)
    #q[e] = .5                     # ambiguous true edge
    q=property_map
    #e = g.add_edge(15, 73)
    #q[e] = .5                     # ambiguous spurious edge

    # We inititialize UncertainBlockState, assuming that each non-edge
    # has an uncertainty of q_default, chosen to preserve the expected
    # density of the original network:
    # sum(q_ij)+sum(qdefault_i'j')=E
    if ((N * (N - 1))/2 - E)==0:
        q_default=0
    else:
        q_default = (E - sum(q)) / ((N * (N - 1))/2 - E)

    state = gt.UncertainBlockState(g, q=q, q_default=q_default)
   
    # We will first equilibrate the Markov chain
    gt.mcmc_equilibrate(state, wait=100, mcmc_args=dict(niter=10))
    
    # Now we collect the marginals for exactly 100,000 sweeps, at
    # intervals of 10 sweeps:
    global u, bs, cs # xin
    u = None              # marginal posterior edge probabilities
    bs = []               # partitions
    cs = []               # average local clustering coefficient
    def collect_marginals(s):
        global bs, u, cs
       
        u = s.collect_marginal(u)
        bstate = s.get_block_state()
        bs.append(bstate.levels[0].b.a.copy())
        cs.append(gt.local_clustering(s.get_graph()).fa.mean())
            
    print('mcmc running..')
    gt.mcmc_equilibrate(state, force_niter=1000, mcmc_args=dict(niter=10),
                        callback=collect_marginals)

    eprob = u.ep.eprob
    return  bs[-1]
