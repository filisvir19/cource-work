import numpy as np

N = 15
M = 30

A = np.random.randint(0,100, (N,M))

m=0
indm=0
for i in range (M):
    if np.sum(A[:, i])>m:
        m = np.sum(A[:, i])
        indm=i
stmax=0

for b in A [: , indm]:
    if b> stmax:
        stmax=b
        
print("Максимальный элемент этого столбца-"+str(stmax))