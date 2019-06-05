import numpy as np

N = 15
M = 30
L = 12
K = 10

A = np.random.randint(-10,10, (N,M))

matrix_bool = A == 0
col = np.sum(matrix_bool, axis=1)
A = np.insert(A, M, col, axis=1)
row = np.append(np.sum(matrix_bool, axis=0), 0)
A = np.insert(A, N, row, axis=0)
print("Полученная матрица:\r\n {}".format(A))