N,M = map(int,input().split())
C = list(map(str,input().split()))
D = list(map(str,input().split()))
P = list(map(int,input().split()))

ans = 0
for i in C:
    id = [k for k,v in enumerate(D) if v == (i)]
    if id == []:
        ans += P[0]
    else:
        ans += P[id[0]+1]

print(ans)