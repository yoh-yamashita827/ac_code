import sys
sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限
dye = set()
def dfs(now):
    dye.add(now)

    for i in range(n):
        if i in dye:
            continue
        if eq(xy[now][0],xy[now][1],xy[i][0],xy[i][1]) <= (d**2):
            dfs(i)

    
    

dfs(0)

for i in range(n):
    if i in dye:
        print('Yes')
    else:
        print('No')


N = int(input())
#N,M = map(int,input().split())
#S = input()
#A = list(map(int,input().split()))

from collections import deque
from collections import defaultdict
edge = defaultdict(list)
for _ in range(N):
   a,b = map(int,input().split())

   edge[a].append(b)
   edge[b].append(a)


stack = deque([1])
visit = set()
ans = []
while stack:
  
   node = stack.pop()
   ans.append(node)

   if node in visit:
      continue
   visit.add(node)
   for child in edge[node]:
      stack.append(child)


print(max(ans))


N,M=map(int,input().split())
E=[[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
  a,b,c=map(int,input().split())
  E[a][b]=c
  E[b][a]=c

ans=0
used=[False]*(N+1)

def dfs(v,s):
  global ans
  used[v]=True
  if s>ans: ans=s
  for i in range(1,N+1):
    if not used[i] and E[v][i]:
      dfs(i,s+E[v][i])
  used[v]=False

for i in range(1,N+1):
  dfs(i,0)

print(ans)
