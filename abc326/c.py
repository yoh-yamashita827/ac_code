# n = int(input())

n,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
a.append(9000000000000)

ans = 0
r = 0
for l in range(0,n):
    while a[r]-a[l] < m:
        r += 1
    ans = max(ans,r-l)

print(ans)
