import numpy as np

N = 15
M = 30
H = 2

A = np.random.randint(-10,10, (N,M))

A_bool = A == H
col_sum = np.sum(A_bool, axis=1)

print("Строки в которых встречается значение {}:".format(H))
print(np.argwhere(col_sum).flatten())

print("Строки в которых нет значения {}:".format(H))
print(np.argwhere(col_sum == 0).flatten())