n,k = map(int,input().split())
s = [int(input()) for i in range(n)]

if 0 in s:
    print(n)
else:
    r, ans, tmp = 0, 0, 1
    for l in range(n):
        while r < n and tmp*s[r] <= k:
            tmp *= s[r]
            r += 1
        ans = max(ans,r-l)
        if l == r:
            r += 1
        else:
            tmp //= s[l]
    print(ans)
    