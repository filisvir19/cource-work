import numpy as np

N = 15

A = np.random.randint(-10,10, (N,N)).astype(float)
print("Матрица:\r\n{}".format(A))

diagonal_elements = [np.diagonal(A, i) for i in [1, -1]]
values = (diagonal_elements[0] + diagonal_elements[1])/2

rng = np.arange(N-1)
A[rng, rng+1] = values[rng]
A[rng+1, rng] = values[rng]

print("Полученная матрица:\r\n{}".format(A))