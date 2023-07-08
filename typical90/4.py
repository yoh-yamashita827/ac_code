h,w = map(int,input().split())
A = []
for _ in range(h):
    A.append(list(map(int,input().split())))

yoko =  list(map(sum, A))
tate = [sum(column) for column in zip(*A)]

for i in range(h):
    ans = []
    for j in  range(w):
        ans.append(yoko[i]+tate[j]-A[i][j])
        # ans.append(yoko[j]+tate[i]-A[i][j])
    print(*ans)