n,x = map(int,input().split())
A = list(map(int,input().split()))

ans = 'Yes'

if x not in A:
    ans = 'No'

print(ans)

