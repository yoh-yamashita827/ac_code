import sys

def dijkstra(graph, start):
    # 初期化
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    distance[start] = 0

    # ダイクストラ法
    for i in range(n):
        # 未処理の中で最小の距離を持つ頂点を探す
        min_distance = sys.maxsize
        for j in range(n):
            if not visited[j] and distance[j] < min_distance:
                min_distance = distance[j]
                u = j

        # 訪問済みにする
        visited[u] = True

        # uから到達可能な頂点の距離を更新する
        for v in range(n):
            if not visited[v] and graph[u][v] != 0:
                new_distance = distance[u] + graph[u][v]
                if new_distance < distance[v]:
                    distance[v] = new_distance

    return distance


n, m = map(int, input().split())


conn = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    conn[a-1][b-1] = -c
    conn[b-1][a-1] = -c

start = 0
# dist = dijkstra(conn,start)


ans = 0
for i in range(n):
    ans = min(ans,min(dijkstra(conn,i)))

print(-ans)