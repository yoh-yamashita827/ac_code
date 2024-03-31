N = int(input())
# N,M = map(int,input().split())
# S = input()
A = list(map(int,input().split()))
Q = int(input())

# S = []
# for _ in range(N):
#    S.append(input())

alpha = 0
from collections import defaultdict
a = defaultdict(int)
for i,v in enumerate(A):
   a[i] = v
base = -1
for i in range(Q):
   query = list(map(int,input().split()))

   if query[0] == 1:   
      base = query[1]
      # flg1 = True
   elif query[0] == 2:
      if base == -1:
         a = a
      else:a = dict(zip(list(range(N)),[base]*N))
      a[query[1]-1] += query[2]
      # flg2 = True

   else:
      # if flg:
      print(a[query[1]-1]+alpha)

      # flg1 = flg2 = False