import numpy as np

N = 15
M = 30

A = np.random.randint(0,100, (N,M))

M_mean = A.mean(axis=0)
N_mean = A.mean(axis=1)
N_mean = np.append(N_mean, None)

A = np.vstack((A, M_mean))
A = np.hstack((A, N_mean.reshape(-1,1)))

print(A)