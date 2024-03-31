n = int(input())

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i].append(int(input())-1)

from collections import deque
que=deque()
que.append((0,0))
seen = set()
ans = [-1]*n
while(que):
    node,dep = que.popleft()
    if node == 1:
        break

    if node in seen:
        continue

    seen.add(node)

    for child in graph[node]:
        if child not in seen:
            ans[child] = dep+1
            que.append((child,dep+1))
    
print(ans[1])


