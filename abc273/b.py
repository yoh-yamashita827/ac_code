N = int(input())
#N,M = map(int,input().split())
#S = input()
A = list(map(int,input().split()))
#S = []
#for _ in range(N):
   # S.append(input())

from collections import defaultdict

manage = defaultdict(int)

for i in A:
   manage[i] = 1

tmp = 0
search = sorted(list(manage.keys()),reverse=True)
for i in search:
   manage[i] += tmp
   tmp = manage[i]

for i,v in enumerate(A):
   print(manage[v]-1)