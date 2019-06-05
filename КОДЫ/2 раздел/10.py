import numpy as np

N = 15
M = 30
K = 10

A = np.random.randint(-10,10, (N,M))
K_m = A[:, K].flat

for i in range(M):
    if i != K:
        for k in range(N):
            A[k, i] = A[k, i] * K_m[k]
print(A)