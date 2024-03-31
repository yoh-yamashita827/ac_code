# n : ノード数
# m : パス数
n, m = map(int, input().split())


conn = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    conn[a-1][b-1] = c
    conn[b-1][a-1] = c


# iノードに訪れたことがある場合はvisited[i] = True
visited = [False] * n


def dfs(now, cost):
    if visited[now]: return 0
    
    visited[now] = True

    for i in range(0, n):
        if conn[now][i]: 
            cost += dfs(i, conn[now][i])

    
    # visited[now] = False

    return cost

ans = 0
for i in range(n):
    ans = max(ans,dfs(i,0))

print(ans)