import numpy as np

N = 15
M = 30

A = np.random.randint(0,2, (N,M))

col = [i % 2 for i in np.sum(A, axis=1)]

A = np.insert(A, M, col, axis=1)

print("Полученная матрица:\r\n {}".format(A))