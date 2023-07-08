n = int(input())
d,x = map(int,input().split())

A = []
for _ in range(n):
    A.append(int(input()))
ans = 0
for i in A:
    ans += (1+int((d-1)/i))

print(ans+x)
