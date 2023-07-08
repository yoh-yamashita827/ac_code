n = int(input())
A = list(map(int,input().split()))

tmp = []
ans = []
for i in A:
    if len(tmp) == 7:
        ans.append((sum(tmp)))
        tmp = []
        tmp.append(i)
    else:
        tmp.append(i)

ans.append(sum(tmp))
print(*ans)
