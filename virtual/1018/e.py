from collections import defaultdict
n = int(input())
A = list(map(int,input().split()))

rem = defaultdict(int)
it = iter(A[1:])
mae = 0
for i,j in zip(it,it):
    rem[j] = (j-i)+mae
    mae = rem[j]

def binary(x,A):
    l = 0
    r = len(A)

    while(r!= l):
        m = (r+l)//2

        if A[m] > x:
            r = m
        elif A[m] < x:
            l = m+1
        else:
            return -1
    return r

q = int(input())

for i in range(q):
    ans = 0
    l,r = map(int,input().split())
    tmp_r = binary(r,A)
    tmp_l = binary(l,A)

    if tmp_r == -1:
        ans = rem[r]

    else:
        ans = abs(rem[r] - r)

    if tmp_l == -1:
        ans -= (rem[l])

    else:
        ans -= abs(rem[l]-l)


    print(ans)