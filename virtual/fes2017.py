N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))

import collections

d = collections.Counter(D)
t = collections.Counter(T)

for key in t.keys():
    if t[key] > d[key]:
        print('NO')
        exit()

print('YES')
