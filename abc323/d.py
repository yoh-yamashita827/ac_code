n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
from collections import defaultdict
slimes = defaultdict(int)
import math

ans = 0
# s = []
for _ in range(n):
    s,c = map(int,input().split())
    slimes[s] = c
if n == 1:
    for i in slimes.values():
        if i >= 2:
            ans += math.ceil(math.log2(i))

        else:
            ans += i

    print(ans)
    exit()
ans = 0
slimes2 = defaultdict(int)
slimes = dict(slimes)
for k,v in slimes.items():
    can_num = (v)//2
    if can_num == 0:
        continue
    if (k*2) in slimes.keys():
        slimes2[k*2] = can_num + slimes[k*2]
    else:
        slimes2[k*2] = can_num
    slimes2[k] = v%2

slimes.update(slimes2)
ans = 0
import math

for i in slimes.values():
    if i >= 2:
        ans += math.ceil(math.log2(i))

    else:
        ans += i

print(ans)