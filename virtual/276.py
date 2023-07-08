N, M = map(int,input().split())
AB = []

for i in range(M):
    AB.append(list(map(int,input().split())))

import bisect
ans = {}
for i in AB:
    bisect.insort(ans.setdefault(i[0],[]),i[1])
    bisect.insort(ans.setdefault(i[1],[]),i[0])

for i in range(1,N+1):
    if i not in ans.keys():
        print(0)
    else:
        print(len(ans[i]),*ans[i])