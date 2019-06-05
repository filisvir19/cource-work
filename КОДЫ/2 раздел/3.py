import numpy as np
import numpy as np

N = 15
M = 30

A = np.random.randint(0,100, (N,M))

mx=0
indmx=0
for i in range (M):
    if np.sum(A[:, i])>mx:
        mx = np.sum(A[:, i])
        indmx=i
print("Столбец с максимальной суммой элементов-"+ str(A[: , indmx]))
print("Сумма этого столбца-"+str(mx)+ ","+ "номер этого столбца-"+ str(indmx+1))
stmin=10
for b in A [: , indmx]:
    if b< stmin:
        stmin=b
print("Минимальный элемент этого столбца-"+str(stmin))