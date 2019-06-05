import numpy as np

N = 15
M = 30

A = np.random.randint(-10,10, (N,M))


N_sum = np.sum(A, axis=1)/np.sum(A)
print("Доля элементов каждой строки-"+str(np.sum(A, axis=1)/np.sum(A)))

A = np.hstack((A, N_sum.reshape(-1,1)))

print(A)