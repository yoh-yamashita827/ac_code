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