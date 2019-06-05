import numpy as np

N = 15
M = 30

A = np.random.randint(-10,10, (N,M))

col = np.sum(A, axis=1) * -1

A = np.insert(A, M, col, axis=1)

print("Полученная матрица:\r\n {}".format(A))