n,m = map(int,input().split())
s = []
t = set()
for _ in range(n):
    s.append(input())
for _ in range(m):
    t.add(input())
cnt = 0
visit = set()
for i in range(n):
    if s[i][3:] in t:
        cnt += 1
print(cnt)