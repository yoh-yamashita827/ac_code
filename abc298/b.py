N = int(input())
A = []
B = []
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    B.append(list(map(int,input().split()))) 

import numpy as np
np_A = np.array(A)
np_B = np.array(B)

roll = np_A.copy()
for _ in range(4):
    roll = roll[::-1].T

    mask = (roll == 1)
    if (np.all(np_B[mask]==1)):
        print('Yes')
        exit()
print('No')

