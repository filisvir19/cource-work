import numpy as np

N = 15
M = 30
L = 12
K = 10

A = np.random.randint(-10,10, (N,M))

parts = [
    A[:L, :K],
    A[:L, K:],
    A[L:, :K],
    A[L:, K:],
]

for i in range(len(parts)):
    print("Cреднее арифметическое {} части: {}".format(i+1, np.average(parts[i])))