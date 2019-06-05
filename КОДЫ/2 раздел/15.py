import numpy as np

N = 15
M = 30
H = 5

A = np.random.randint(-10,10, (N,M))

A_bool = A == H
row_sum = np.sum(A_bool, axis=0)

print("Столбцы в которых встречается значение {}:".format(H))
print(np.argwhere(row_sum).flatten())

print("Столбцы в которых нет значения {}:".format(H))
print(np.argwhere(row_sum == 0).flatten())