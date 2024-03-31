n,l = map(int,input().split())
mod = 10**9 + 7
dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1


for i in range(2,n+1):
    if i >= l:
        dp[i] = dp[i-1] + dp[i-l]
    else:
        dp[i] = dp[i-1]

print(dp[-1]%mod)