import heapq
from collections import defaultdict

n = int(input())

edge = defaultdict(int)

d = []
for i in range(n-1):
    d.append(([0]*(i+1))+list(map(int,input().split())))

for i in range(n-1):
    for j in range(n):
        if d[i][j] == 0:continue
        edge[(i,j)] = d[i][j]

heap = dict(sorted(edge.items(),key=lambda x:x[1],reverse=True))

ans = 0
visit = set()
for key in heap.keys():
    if (key[0] in visit) or (key[1] in visit):
        continue
    ans += edge[key]
    visit.add(key[0])
    visit.add(key[1])

print(ans)