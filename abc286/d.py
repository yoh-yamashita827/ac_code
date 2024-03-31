from collections import defaultdict
n,x = map(int,input().split())

AB = []
money = defaultdict(int)
for _ in range(n):
   a,b = map(int,input().split())   
   money[a] += b

a = 1