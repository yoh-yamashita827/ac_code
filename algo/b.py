#N = int(input())
N,M = map(int,input().split())
#S = input()
#A = list(map(int,input().split()))
AB = []


from collections import deque
from collections import defaultdict
edge = defaultdict(list)
for _ in range(M):
   a,b = map(int,input().split())

   edge[a].append(b)
   # edge[b].append(a)


def dfs(start):
   stack = deque([start])
   visit = set()
   
   while stack:
   
      node = stack.pop()
 
      if node in visit:
         continue
      visit.add(node)
      if len(visit) == N:
         return True
      for child in edge[node]:
         stack.append(child)

   return False

for i in range(1,N+1):
   if dfs(i):
      print(i)
      exit()
print(-1)


   
