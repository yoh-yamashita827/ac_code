from collections import defaultdict
n,m = map(int,input().split())
# edge = [[0]*n for _ in range(n)]
edge = defaultdict(list)

for _ in range(m):
    a,b = map(int,input().split())
    if a > b:
        a,b = b,a
    edge[b-1].append(a-1)
    # edge[b-1][a-1] = 1

ans = 0
for i in enumerate(edge.values()):
    if (len(i[1]) == 1):
        ans += 1

print(ans)