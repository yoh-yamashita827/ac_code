# 入力を受け取る
n,m = map(int,input().split())
S = [input() for _ in range(n)]

from heapq import heapify,heappop,heappush
INF=float('inf')

## コスト行列を作成
cost = [[[INF]*m for _ in range(n)] for _ in range(61)]

hq = []
g_x = g_y = 0

## スタートの位置を求め，その位置のコストを0に設定
for i in range(n):
    for j in range(m):
        if S[i][j] == 'S':
            # 
            heappush(hq,(i,j,0))
            cost[0][i][j] = 0

## ゴールの位置を求める
for i in range(n):
    for j in range(m):
        if S[i][j] == 'G':
            g_x = i
            g_y = j

## 4つの移動方向を定義            
walk=[
    (1,0),
    (-1,0),
    (0,1),
    (0,-1),
]

while(hq):

    i,j,k = heappop(hq)
    if k >= 60:
        continue
    for x,y in walk:
        if (0 <= (i+x) < n) and (0 <= (j+y) < m):
            
            if S[i+x][j+y] == '#':
                if cost[k][i][j]+(k+1) < cost[k+1][i+x][j+y]:
                    cost[k+1][i+x][j+y] = cost[k][i][j] + (k+1)
                    heappush(hq,(i+x,j+y,k+1))

            else:
                if cost[k][i][j]+(1) < cost[k][i+x][j+y]:
                    cost[k][i+x][j+y] = cost[k][i][j]+1
                    heappush(hq,(i+x,j+y,k))

ans = INF         
for i in range(61):
    ans = min(ans,cost[i][g_x][g_y])
print(ans)