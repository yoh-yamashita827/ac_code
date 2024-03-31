# n = int(input())
from collections import deque
n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
edge = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    edge[a-1][b-1] = c
    edge[b-1][a-1] = c


def dfs(start):
    stack = deque((start,0))
    visit = set()
    pre = -1
    cnt = 0
    while stack:  
        node = stack.pop()

        if node in visit:
            continue
        visit.add(node)
        # if pre != -1:
        #     cnt += edge[pre][node]
        # pre = node
        for child,c in enumerate(edge[node]):
            if c == 0:
                continue
            stack.append(child)
    return cnt

ans = 0
for i in range(n):
    ans = max(ans,dfs(i))

print(ans)

