import sys
sys.setrecursionlimit(10**7)

H,W=map(int,input().split())
C=[]
dxdy=[(0,1),(0,-1),(1,0),(-1,0)]
for _ in range(H):
    c=input()
    C.append(c)
mp=[[-1]*W for _ in range(H)]
visited=[[-1]*W for _ in range(H)]
dist=[[-1]*W for _ in range(H)]
ans = -1
def dfs(y,x,d):
    global ans # グローバル変数
    global visited
    
    if mp[y][x] == 0 and dist[y][x]!=0:
        return
    if C[y][x] == "#":
        return
    if dist[y][x]==0:
        ans = max(ans,d)
        return
        
    
    mp[y][x] = 0
    visited[y][x]=0
    if dist[y][x]!=0:
        dist[y][x]=d
    #print(y,x,dist[y][x])
    for dx, dy in dxdy:
        ny = y + dy
        nx = x + dx
        if 0<=nx<W and 0<=ny<H and C[ny][nx]==".":
            dfs(ny, nx, d+1)
    mp[y][x] = -1
    dist[y][x]=-1
        
for n in range(H):
    for m in range(W):
        dfs(n,m,0)
if ans<=2:
    print(-1)
else:
    print(ans)


