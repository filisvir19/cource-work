import numpy as np

N = 15

A = np.random.randint(-10,10, (N,N))

elements = np.diagonal(A, 1)

print("Элементы, расположенные выше главной диагонали:")
print(elements)
print("Сумма элементов, расположенных выше главной диагонали:")
print(np.sum(elements))
elements = np.diagonal(A[::-1], -1)
print("Элементы, расположенные выше побочной диагонали:")
print(elements)
print("Произведение элементов, расположенных выше побочной диагонали:")
print(np.prod(elements))