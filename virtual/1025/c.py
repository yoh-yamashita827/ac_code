# n = int(input())
n,q = map(int,input().split())
# s = input()
A = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

from collections import defaultdict
number = defaultdict(list)

for i,v in enumerate(A):
    number[v].append(i)

for i in range(q):
    x,k = map(int,input().split())
    app = number[x]
    if len(app) < k:
        print(-1)
    else:
        print(app[k-1]+1)