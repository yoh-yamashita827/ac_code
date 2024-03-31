# n = int(input())
n,m = map(int,input().split())
s = input()
c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#    s.append(input())
from collections import defaultdict
color = defaultdict(list)

for i,v in enumerate(c):
   color[v].append(i)

ans = [0]*n
for i in color.values():
   id = [i[-1]]+(i[0:-1])
   for j,v in enumerate(id):
      ans[i[j]] = s[v]

print(''.join(ans))