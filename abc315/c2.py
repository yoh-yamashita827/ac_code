n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
from collections import defaultdict
dic =  defaultdict(list)
f = []
s = []
for _ in range(n):
   a,b = map(int,input().split())
   f.append(a)
   s.append(b)
   dic[a].append(b)

max_s = -1
max_f = -1
for k,v in dic.items():
    if max_s < max(v):
        max_s = max(v)
        max_f = k
        
tmp = sorted(dic[max_f])
if len(tmp)==1:
    ans1 = -1
else:
    ans1 = max_s + tmp[-2]//2

max_s2 = -1
for k,v in dic.items():
    if k == max_f:
        continue

    if max_s2 < max(v):
        max_s2 = max(v)

ans2 = max_s + max_s2

print(max(ans1,ans2))