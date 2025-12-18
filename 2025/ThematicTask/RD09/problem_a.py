import numpy as np
import scipy as sp
from typing import Tuple

def init_matrices(N: int, prob_nonzero: float) -> Tuple[np.ndarray, sp.sparse.csr_array]:
    assert 0.0 <= prob_nonzero <= 1.0
    np.random.seed(0)
    A_dense = np.random.rand(N, N)
    assert A_dense.dtype == np.double
    mask = np.random.rand(N, N) < prob_nonzero
    A_dense *= mask

    elems = []
    for i in range(N):
        for j in range(N):
            if mask[i, j]:
                elems.append((i, j, A_dense[i, j]))
    row_ind = np.array([e[0] for e in elems])
    col_ind = np.array([e[1] for e in elems])
    data = np.array([e[2] for e in elems])
    A_sparse = sp.sparse.csr_array((data, (row_ind, col_ind)), shape=(N, N), dtype=np.double)
    return A_dense, A_sparse
