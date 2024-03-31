import numpy as np
n,d = map(int,input().split())
S = []
for _ in range(n):
    S.append(list(input()))

np_S = np.array(S)
S_T = np_S.T

r, ans, tmp = 0, 0, 1
for l in range(d):
    while r < d and np.all(S_T[r]=='o'):
        r += 1
    ans = max(ans,r-l)
    if l == r:
        r += 1





print(ans)