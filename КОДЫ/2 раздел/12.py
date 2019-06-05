import numpy as np

N = 15
M = 30
K = 10

A = np.random.randint(-10,10, (N,M))
A = np.array(A, float)

for i in range(N):
    mx = np.max(A[i, :])
    for k in range(M):
        if A[i, k] != mx:
            A[i, k] = round(A[i, k] / mx, 2)
print(A)