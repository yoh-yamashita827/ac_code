n,k = map(int,input().split())
A = list(map(int,input().split()))

A.sort()
A = set(A)
base = 0
ans = set()

while ((len(ans) < k)):
    if base in A:
        ans.add(base)
        base += 1
    else:
        print(base)
        exit()

print(base)