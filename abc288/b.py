n,k = map(int,input().split())
s = []
for _ in range(k):
    s.append(input())

s.sort()

for i in range(k):
    print(s[i])