n,m = map(int,input().split())
A = []
for _ in range(m):
    A.append(list(map(int,input().split())))

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

c = cmb(n, 2)

friend = []

for i in range(m):
    for j in range(n-1):
        if ((A[i][j],A[i][j+1]) in friend) or  ((A[i][j+1],A[i][j]) in friend):
            continue
        friend.append((A[i][j],A[i][j+1]))

print(c-len(friend))
