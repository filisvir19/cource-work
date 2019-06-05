import numpy as np

N = 15
M = 30

A = np.random.randint(-10,10, (N,M))

B=np.sum(A)

M_sum = np.sum(A, axis=0)/np.sum(A)
print("Доля элементов каждого столбца-"+str(np.sum(A, axis=0)/np.sum(A)))

A = np.vstack((A,M_sum))

print(A)