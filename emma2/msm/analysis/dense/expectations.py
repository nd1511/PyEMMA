"""This module provides dense implementations for the computation of
expectation values for a given transition matrix."""

import numpy as np

def expected_counts(p0, T, N):
    r"""Compute expected transition counts for Markov chain after N steps. 
    
    Expected counts are computed according to ..math::
    
    E[C_{ij}^{(n)}]=\sum_{k=0}^{N-1} (p_0^T T^{k})_{i} p_{ij}   
    
    Parameters
    ----------
    p0 : (M,) ndarray
        Starting (probability) vector of the chain.
    T : (M, M) ndarray
        Transition matrix of the chain.
    N : int
        Number of steps to take from initial state.
        
    Returns
    --------
    EC : (M, M) ndarray
        Expected value for transition counts after N steps. 
    
    """
    EC=np.zeros(T.shape)
    if(N<=0):
        return EC
    else:
        """Probability vector after (k=0) propagations"""                     
        p_k=1.0*p0
        """Sum of vectors after (k=0) propagations"""
        p_sum=1.0*p_k           
        for k in np.arange(N-1):
            """Propagate one step p_{k} -> p_{k+1}"""
            p_k=1.0*np.dot(p_k,T)      
            """Update sum"""
            p_sum+=p_k             
        """Expected counts"""
        EC=p_sum[:,np.newaxis]*T     
        return EC
    