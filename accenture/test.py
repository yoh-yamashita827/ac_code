from collections import deque

n = int(input())
q = int(input())

grid = [['.']*n for _ in range(n)]

walk=[
    (1,0),
    (-1,0),
    (0,1),
    (0,-1),
]
visited = set()
moves = set()

def move_path2(r0, c0, k0, t0):
    que = deque([(r0, c0, k0, t0)])
    while que:
        r, c, k, t = que.pop()
        if grid[r][c] == '#' and k == t:
            return

        grid[r][c] = '#'
        if k > t:
            for x, y in walk:
                if 0 <= (r+x) < n and 0 <= (c+y) < n:
                    que.append((r+x, c+y, k, t+1))
                    moves.add((r+x, c+y))

for i in range(q):
    r,c,k = map(int,input().split())
    move_path2(r-1,c-1,k,0)

for i in moves:
    x,y = i[0],i[1]
    grid[x][y] = '#'

for i in grid:
    print(''.join(i))

