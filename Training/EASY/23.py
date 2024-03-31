a,b,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

cool = {}
hot = {}

for i in range(a):
    cool[i+1] = A[i]
for i in range(b):
    hot[i+1] = B[i]

ans = min(A)+min(B)
for _ in range(m):
    x,y,c = map(int,input().split())
    ans = min(ans,cool[x]+hot[y]-c)

print(ans)