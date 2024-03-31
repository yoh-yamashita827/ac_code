# n = int(input())
h,w = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
c = []
for _ in range(h):
   c.append(list(input()))

import copy
import numpy as np
map = copy.deepcopy(c)

c = np.array(c)
map = np.array(map)

flg = True
tate = c
while(flg):
    flg = False
    yoko = []
    for i in tate:
        mask = (i != '.')
        tmp = i[mask]
        if len(tmp) >= 2 and np.all(tmp==tmp[0]):
            yoko.append(np.where(i==tmp[0],'.',i))
            flg = True
        else:
            yoko.append(i)
            
    yoko = np.array(yoko)

    flg = False
    tate = []
    for i in yoko.T:
        mask = (i != '.')
        tmp = i[mask]
        if len(tmp) >= 2 and np.all(tmp==tmp[0]):
            tate.append(np.where(i==tmp[0],'.',i))
            flg = True
        else:
            tate.append(i)
            
    tate = np.array(tate)
    tate = tate.T



ans = 0
for i in tate:
    ans += sum(i!='.')

print(ans)
