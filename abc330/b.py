# n = int(input())
n,l,r = map(int,input().split())
# s = input()
A = list(map(int,input().split()))
# s = [input() for _  in range(n)]
ans = []
for i in A:
    if i < l:
        ans.append(l)
    elif i > r:
        ans.append(r)
    else:
        ans.append(i)

print(*ans)