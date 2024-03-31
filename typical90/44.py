n,q = map(int,input().split())
A = list(map(int,input().split()))
from collections import defaultdict
num = defaultdict(int)
for i in range(n):
    num[i] = A[i]
id = 0
for _ in range(q):
    t,x,y = map(int,input().split())

    if t == 1:
        num[(x+id-1)%n],num[(y+id-1)%n] = num[(y+id-1)%n],num[(x+id-1)%n]

    elif t == 2:
        id -= 1

    else:
        print(num[(x+id-1)%n])