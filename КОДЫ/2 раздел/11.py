import numpy as np

N = 15
M = 30
L = 12

A = np.random.randint(-10,10, (N,M))

L_m = A[L, :].flat

for i in range(N):
    if i != L:
        for k in range(M):
            A[i, k] = A[i, k] + L_m[k]
print(A)