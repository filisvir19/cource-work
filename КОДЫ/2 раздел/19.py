import numpy as np

N = 15

A = np.random.randint(-10,10, (N,N))

diagonal_elements = np.array([np.diagonal(A, i) for i in [1, -1]]).flatten()
print("Элементы, расположенные параллельно главной диагонали:")
print(diagonal_elements)

print("Сумма элементов, расположенные параллельно главной диагонали:")
print(np.sum(diagonal_elements))
