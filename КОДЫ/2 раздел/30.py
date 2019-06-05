import numpy as np

N = 15
M = 30

A = np.random.randint(-10,10, (N,M))

row = np.sum(A, axis=0) * -1

A = np.insert(A, N, row, axis=0)

print("Полученная матрица:\r\n {}".format(A))