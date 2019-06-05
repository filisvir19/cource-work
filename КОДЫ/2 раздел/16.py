import numpy as np

N = 15
M = 30
L = 12

A = np.random.randint(-10,10, (N,M))

A = np.delete(A, L, axis=0)

print("Полученная матрица:\r\n {}".format(A))