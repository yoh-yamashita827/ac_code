# 再帰回数の上限を増やしておく必要がある
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

# 木の情報を2次元リストに格納
N, X, Y = map(int, input().split())
X, Y = X - 1, Y - 1
g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
    
# 地点 i の１つ前（の深さ）の地点
prev = [-1] * N
# DFS(今いる場所n, 前にいた場所p)
def DFS(n, p):
    # 今いる場所から、行ける場所
    for nv in g[n]:
        # 行ける所が前にいた場所ならスルー
        if nv == p:
            continue
        # 行ける場所に対する「前の場所」として現地点nを格納
        prev[nv] = n
        # 行ける場所=>今いる場所/今いる場所=>前にいた場所
        DFS(nv, n)

# 前にいた場所は適当に-1としておく        
DFS(Y, -1)
# 出力のための操作
now = X
path = [X + 1]
while prev[now] != -1:
    # さかのぼっていく
    now = prev[now]
    path.append(now + 1)
print(*path)    