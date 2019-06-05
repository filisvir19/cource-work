import numpy as np

N = 15
M = 30
K = 10
L = 12

A = np.random.randint(-10,10, (N,M))


New_A = A[:L, :K]

print(A)

print(np.sum(New_A == 0))