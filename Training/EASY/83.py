n = int(input())
A = [list(map(int,input().split())) for i in range(2)]

ans = INF=float('inf')
from collections import deque
que=deque()
walk=[
    (1,0),
    (0,1)
]
visit=[[False]*n for i in range(2)]
print(visit)
visit[0][0] = True
que.append((0,0))
ans = A[0][0]
while(que):
    # print(que)
    i,j = que.popleft()
    if (i,j) == (1,n-1):break
    for x,y in walk:
        if (visit[i][j]) and ((i+x) < 2) and ((j+x) < n):
            print(i+x,j+y)
            visit[i+x][j+y] = True
            ans += A[i+x][j+y]
            que.append((i+x,j+y))

print(ans)