from collections import deque
que=deque()

n = int(input())
q = int(input())
for i in range(q):
    r,c,k = map(int,input().split())
    que.append((r-1,c-1,k,0))

grid = [['.']*n for _ in range(n)]

walk=[
    (1,0),
    (-1,0),
    (0,1),
    (0,-1),
]
visited = set()
while(que):
    r,c,k,t = que.popleft()
    if grid[r][c] == '#' and k == t:
        continue

    grid[r][c] = '#'
    for x,y in walk:
        if  (0 <= (r+x) < n) and (0 <= (c+y) < n):
            if k > t:
                que.append((r+x,c+y,k,t+1))


for i in grid:
    print(''.join(i))

