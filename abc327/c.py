from collections import defaultdict
import numpy as np
# n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
s = [list(map(int,input().split())) for _  in range(9)]
# for _ in range(n):
#     s.append(input())

from collections import defaultdict
import copy

S = (np.array(s))
SS = copy.deepcopy(S)
for i in SS:
    i.sort()
    if  np.any(i != np.arange(1,10)):
        print('No')
        exit()

SS = copy.deepcopy(S)
for i in SS.T:
    i.sort()
    if  np.any(i != np.arange(1,10)):
        print('No')
        exit()

SS = copy.deepcopy(S)
for i in range(0,9,3):
    for j in range(0,9,3):
        window = SS[i:i+3,j:j+3].reshape(-1)
        window.sort()
        if  np.any(window != np.arange(1,10)):
            print('No')
            exit()

print('Yes')

