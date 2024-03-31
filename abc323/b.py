n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
s = [input() for i in range(n)]
# for _ in range(n):
#     s.append(input())

from collections import defaultdict

victory = defaultdict(int)

for i,v in enumerate(s):
    victory[i+1] = v.count('o')

ans = dict(sorted(victory.items(),key=lambda x : x[1],reverse=True))

print(*list(ans.keys()))

