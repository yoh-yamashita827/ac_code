n = int(input())
a = list(map(int,input().split()))
from collections import deque
ans = 0
a.sort(reverse=True)
for i,v in enumerate(a):
    if i%3== 1:
        ans += v

print(ans)