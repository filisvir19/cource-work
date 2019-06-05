import numpy as np

N = 15
M = 30

A = np.random.randint(-10,10, (N,M))


col_max = np.max(A, axis=0)
A = A / col_max

print("Полученная матрица:\r\n {}".format(A))