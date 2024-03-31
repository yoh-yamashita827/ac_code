n = int(input())
k = int(input())
X = list(map(int,input().split()))

ans = 0
for x in X:
    tmp = min(x,abs(k-x))
    ans += (2*tmp)

print(ans)