import numpy as np
import numpy as np

N = 15
M = 30

A = np.random.randint(0,100, (N,M))

print(A)

mx=10
aver=0
for i in range (N):
    if np.mean (A[i , :])< mx:
        mx= np.mean(A[i , :])
        aver=i

print("Строка с минимальным средним значением элементов-"+ str(A[aver , :]))
print("Среднее значение этой строки-"+str(mx)+ ","+ "номер этой строки-"+ str(aver+1))