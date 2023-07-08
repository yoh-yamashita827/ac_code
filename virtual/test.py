N ,l = map(int,input().split())
import numpy as np
tmp = [['.']*l]*l
grid = np.array(tmp)

for i in range(N):
    a,b,c,d = map(int,input().split())

    if a == c:
        for i in range(b):
            grid[i][a] = '#'
    if b == d:
        for i in range(a):
            grid[b][i] = '#'

print()
