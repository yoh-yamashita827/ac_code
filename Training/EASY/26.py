import math
h = int(input())
dep = int(math.log2(h))
ans = 0
for i in range(dep+1):
    ans += (2**i)

print(ans)