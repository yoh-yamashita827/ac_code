n = int(input())
A = list(map(int,input().split()))

A.sort()
m = []
import math
for i in A:
    cnt = 0
    while(i %2 != 1):
        i //= 2
        cnt += 1
    m.append(cnt)

print(min(m))

    