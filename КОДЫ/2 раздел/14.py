import numpy as np

N = 15
M = 30

A = np.random.randint(-10,10, (N,M))

max_el = np.max(A)
A = A / max_el
print("Полученная матрица:\r\n {}".format(A))