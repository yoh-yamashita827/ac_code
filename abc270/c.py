#N = int(input())
N,X,Y = map(int,input().split())
#S = input()
#A = list(map(int,input().split()))
from collections import deque
from collections import defaultdict
edge = defaultdict(list)
for _ in range(N-1):
   u,v = map(int,input().split())
   edge[u].append(v)
   edge[v].append(u)


stack = deque([X])
visit = set()
root = []
while stack:
   
   node = stack.pop()
   root.append(node)
   if node == Y:
      break
   if node in visit:
      continue
   visit.add(node)
   for child in edge[node]:
      stack.append(child)

ans = []
for i in root[::-1]:
   if i != X:
      ans.append(i)

   else:
      ans.append(X)
      break

print(*ans[::-1])

