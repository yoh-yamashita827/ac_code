from collections import deque
n,m = map(int,input().split())  # 頂点 = n ,辺 = m 

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1]*(n+1)
dist[0] = 0
dist[1] = 0

d = deque()
d.append(1)

while(d):
    v = d.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v]+1
        d.append(1)

ans = dist[1:]
print(*ans,sep = "\n")    #distance