n,k,m = map(int,input().split())

A = list(map(int,input().split()))

sum_a = sum(A)


tmp = ((n*m))-sum_a
if tmp > k:
    print(-1)
    exit()
if tmp > 0:
    print(tmp)
else:
    print(0)