import numpy as np

N = 15
M = 30
K = 10

A = np.random.randint(-10,10, (N,M))

A = np.delete(A, K, axis=1)

print("Полученная матрица:\r\n {}".format(A))
