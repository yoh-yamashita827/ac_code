N = int(input())
XY = []
X = []
Y = []
"""
dp

"""
for _ in range(N):
    XY.append(list(map(int,input().split())))

for i in range(N):
    X.append(XY[i][0])
    Y.append(XY[i][1])

dp = [[0,1] for _ in range(N+1)]

dp[0][0] = 0
dp[0][1] = 0
     
for i in range(1,N+1):
    if X[i-1] == 0:
        dp[i][0] = max(dp[i-1][0],dp[i-1][0]+Y[i-1],dp[i-1][1]+Y[i-1])
        dp[i][1] = dp[i-1][1]

    else:
        dp[i][0] = (dp[i-1][0])
        dp[i][1] = max(dp[i-1][1],dp[i-1][0]+Y[i-1])

    
print(max(dp[-1]))

