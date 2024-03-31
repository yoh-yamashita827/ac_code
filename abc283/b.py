n = int(input())
# n,m = map(int,input().split())
# s = input()
a = list(map(int,input().split()))
q = int(input())
# s = []
# for _ in range(n):
#     s.append(input())
from collections import defaultdict
A = defaultdict(int)

for i,v in enumerate(a):
    A[i] = v

for i in range(q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        A[query[1]-1] = query[2]

    else:
        print(A[query[1]-1])