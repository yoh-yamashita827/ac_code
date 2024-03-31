# n = int(input())
n,s,m,l = map(int,input().split())
# s = input()
# A = list(map(int,input().split()))
# s = [input() for _  in range(n)]

ans = INF=float('inf')

for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            if n <= (i*6)+(j*8)+(k*12):
                ans = min(ans,((s*i)+(m*j)+(l*k)))

print(ans)