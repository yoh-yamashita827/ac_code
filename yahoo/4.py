
n,m = map(int,input().split())
S = [input() for _ in range(n)]

from heapq import heapify,heappop,heappush
INF=float('inf')
cost = [[[INF]*m for _ in range(n)] for _ in range(901)]

hq = []
g_x = g_y = 0
for i in range(n):
    for j in range(m):
        if S[i][j] == 'S':
            heappush(hq,(0,i,j,0))
            cost[0][i][j] = 0

for i in range(n):
    for j in range(m):
        if S[i][j] == 'G':
            g_x = i
            g_y = j
walk=[
    (1,0),
    (-1,0),
    (0,1),
    (0,-1),
]

while(hq):
    c,i,j,k = heappop(hq)
    if k >= 900:
        continue
    # print(c,i,j,k)
    for x,y in walk:
        if (0 <= (i+x) < n) and (0 <= (j+y) < m):
            
            if S[i+x][j+y] == '#':
                if cost[k][i][j]+(k+1) < cost[k+1][i+x][j+y]:
                    cost[k+1][i+x][j+y] = cost[k][i][j] + (k+1)
                    heappush(hq,(cost[k+1][i+x][j+y],i+x,j+y,k+1))

            else:
                if cost[k][i][j]+(1) < cost[k][i+x][j+y]:
                    cost[k][i+x][j+y] = cost[k][i][j]+1
                    heappush(hq,(cost[k][i+x][j+y],i+x,j+y,k))

ans = INF         
for i in range(901):
    ans = min(ans,cost[i][g_x][g_y])
print(ans)

    


# from collections import deque
# que=deque()

# n = int(input())
# q = int(input())
# for i in range(q):
#     r,c,k = map(int,input().split())
#     que.append((r-1,c-1,k,0))

# # 地図の初期化
# grid = [['.']*n for _ in range(n)]

# # 移動する範囲
# walk=[
#     (1,0),
#     (-1,0),
#     (0,1),
#     (0,-1),
#     ]

# # 既に訪れているか
# visited = set()

# # 幅優先探索する
# while(que):
#     r,c,k,t = que.popleft()
#     if grid[r][c] == '#' and k == t:
#         continue

#     grid[r][c] = '#'
#     for x,y in walk:
#         if  (0 <= (r+x) < n) and (0 <= (c+y) < n):
#             if k > t:
#                 que.append((r+x,c+y,k,t+1))


# for i in grid:
#     print(''.join(i))

