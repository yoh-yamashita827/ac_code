n,x,y = map(int,input().split())

E = set()
# adj = [[] for i in range(n + 1)]
for _ in range(n-1):
    u,v= (map(int,(input().split())))
    # adj[u].append(v)
    E.add((u,v))

import sys
sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限
import copy
visit = [False]*n

def expand(node):
    ans = []
    for i in E:
        if node in i:
            ans.append(i)
    return ans

path = []
visit = set()
ans = []
def dfs(now):
    path.append(now)
    visit.add(now)
    if len(visit) == n-1:
        ans.append(path)
    
    for i in expand(now):
        dfs(i)

anss = dfs(x)

for i in anss:
    if (i[0] == x) and (i[-1] == y):
        print(i)
        exit()



