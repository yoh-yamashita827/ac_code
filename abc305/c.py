h,w = map(int,input().split())

S = []
for _ in range(h):
    S.append(list(input()))

yoko = []
for i in S:
    yoko.append(i.count('#'))

import numpy as np
tate = []
transpose = np.array(S).T
for i in transpose:
    tate.append(list(i).count('#'))


ans = 1000
x = 0
y = 0
for id,i in enumerate(yoko):
    if i == 0:
        continue

    if ans > i:
        ans = i
        y = id

ans = 1000
for id,i in enumerate(tate):
    if i == 0:
        continue

    if ans > i:
        ans = i
        x = id     

print(y+1,x+1)  

