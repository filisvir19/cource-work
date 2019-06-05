import numpy as np

N = 15
M = 30

A = np.random.randint(-10,10, (N,M))

M_sum = (A < 0).sum(axis=0)
N_sum = (A < 0).sum(axis=1)

N_sum = np.append(N_sum, None)

A = np.vstack((A, M_sum))
A = np.hstack((A, N_sum.reshape(-1,1)))

print(A)