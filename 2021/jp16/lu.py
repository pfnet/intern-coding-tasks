#!/usr/bin/env python3
import argparse
from typing import Any, Tuple

import numpy as np
import torch
from scipy.linalg import lu as scipy_lu
from torch import Tensor


@torch.jit.script
def lu(mat: Tensor, tensor_blocksize: Tensor) -> Tuple[Tensor, Tensor, Tensor]:
    mat = mat.clone()
    N = mat.shape[0]
    blocksize = int(tensor_blocksize)
    P = torch.eye(N, dtype=mat.dtype)
    L = torch.zeros_like(mat)
    U = torch.zeros_like(mat)

    for n in range(0, N, blocksize):
        rb = cb = n
        re = ce = n + blocksize

        for row in range(rb, re):
            col = row
            row_swap = int(torch.argmax(torch.abs(mat[row:, col]))) + row
            if row_swap > row:
                mat[[row, row_swap], :] = mat[[row_swap, row], :]
                P[[row, row_swap], :] = P[[row_swap, row], :]
                L[[row, row_swap], :col] = L[[row_swap, row], :col]
            L[row:, col] = mat[row:, col] / mat[row, col]
            U[row, col:ce] = mat[row, col:ce]
            mat[row + 1 :, col + 1 : ce] -= (
                L[row + 1 :, col : col + 1] @ U[row : row + 1, col + 1 : ce]
            )

        U[rb:re, ce:] = torch.linalg.inv(L[rb:re, cb:ce]) @ mat[rb:re, ce:]
        mat[re:, ce:] -= L[re:, cb:ce] @ U[rb:re, ce:]

    return P.T, L, U


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=4)
    parser.add_argument("--blocksize", type=int, default=2)
    parser.add_argument("--rtol", type=float, default=1e-5)
    parser.add_argument("--atol", type=float, default=1e-8)
    args = parser.parse_args()

    assert args.N % args.blocksize == 0, "N must be a multiple of blocksize"

    np.random.seed(42)

    while True:
        A = np.random.rand(args.N, args.N)
        if np.abs(np.linalg.det(A)) > 0.01:
            break

    tensor_A = torch.from_numpy(A).clone()
    tensor_blocksize = torch.tensor(args.blocksize)

    trace = torch.jit.trace(lu, (tensor_A, tensor_blocksize))  # type: ignore
    graph = trace.inlined_graph
    graph_opt = trace.graph_for(tensor_A, tensor_blocksize)

    with open("graph.txt", "w") as f:
        f.write(str(graph))

    with open("graph_opt.txt", "w") as f:
        f.write(str(graph_opt))

    P, L, U = scipy_lu(A)
    tensor_P, tensor_L, tensor_U = trace(tensor_A, tensor_blocksize)

    def verify(x: Any, tensor_x: Tensor) -> bool:
        return bool(
            np.allclose(x, tensor_x.detach().numpy(), rtol=args.rtol, atol=args.atol)
        )

    passed = verify(P, tensor_P) and verify(L, tensor_L) and verify(U, tensor_U)

    print(f"Verify (rtol={args.rtol}, atol={args.atol}):", "OK" if passed else "FAIL")
