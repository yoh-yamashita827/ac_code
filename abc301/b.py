N = int(input())
A = list(map(int,input().split()))
ans = []
for i in range(len(A)-1):
    now = A[i]
    next = A[i+1]
    if abs(now-next) == 1:
        ans.append(now)
        continue
    if next-now > 0:
        for j in range(now,next):
            ans.append(j)
    else:
        while(now > next):
            ans.append(now)
            now -= 1

ans.append(A[-1])
print(*ans)
