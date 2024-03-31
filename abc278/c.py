#N = int(input())
N,Q = map(int,input().split())
#S = input()
#A = list(map(int,input().split()))

from collections import defaultdict
follow = defaultdict(set)
for _ in range(Q):
   t,a,b = (map(int,input().split()))

   if t == 1:
      follow[a].add(b)
   elif t == 2:
      if b in follow[a]:
         follow[a].remove(b)

   elif t == 3:
      if (b in follow[a]) and (a in follow[b]):
         print('Yes')
      else:
         print('No')