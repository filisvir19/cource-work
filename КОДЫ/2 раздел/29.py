import numpy as np

N = 15
M = 30
K = 10

A = np.random.randint(-10,10, (N,M))
A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(A))

col = np.random.randint(low=-9, high=10, size=N)
print("Столбец для вставки: {}".format(col))

A = np.insert(A, K, col, axis=1)
print("Полученная матрица:\r\n {}".format(A))