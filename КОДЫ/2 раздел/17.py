import numpy as np

N = 15
M = 30
K = 10
L = 12

A = np.random.randint(-10,10, (N,M))
row = np.random.randint(low=-9, high=10, size=M)

A = np.insert(A, L, row, axis=0)

print("Полученная матрица:\r\n {}".format(A))