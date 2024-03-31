n,m,c=map(int,input().split())
b = list(map(int,input().split()))
a = [list(map(int,input().split())) for _ in range(n)]

cnt = 0

for i in a:
    tmp = 0
    for aa,bb in zip(b,i):
        tmp += (aa*bb)
    if tmp+c>0:
        cnt += 1
print(cnt)