N,X = map(int,input().split())
T = list(map(int,input().split()))

# 次使用する配列に今回の結果を残すので+1している
dp = [[0]*(X+1) for i in range(N+1)] # DPの配列作成

for i in range(N):
    for j in range(X+1):
        if j < T[i]: # この時点では許容量を超えていないので選択しない
            dp[i+1][j] = dp[i][j] # ただ選択はしていないが、今回の情報をそのままi+1の方へ移す
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-T[i]]+T[i])

ans = dp[N][X]+1
mod = 998244353
x =  pow(27, -1, mod)
print(ans * x % mod)
