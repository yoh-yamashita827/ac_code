n = int(input())
p = list(range(1,n+1))
p = p[::-1]
# print(p)
ans = 0
for i in range(n):
    ans += (i+1)%p[i]

print(ans)