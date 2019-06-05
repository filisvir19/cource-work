import numpy as np

N = 15
M = 30

A = np.random.randint(-10,10, (N,M))

diagonal_main = np.diagonal(A)
print("Элементы главной диагонали:\r\n{}".format(diagonal_main))

sum_diagonal_main = np.sum(diagonal_main)
print("Cумма элементов главной диагонали:\r\n{}".format(sum_diagonal_main))

diagonal_side = np.diagonal(A[::-1])
print("Элементы побочной диагонали:\r\n{}".format(diagonal_side))

sum_diagonal_side = np.sum(diagonal_side)
print("сумму элементов побочной диагонали:\r\n{}".format(sum_diagonal_side))