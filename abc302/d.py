n,m,d = map(int,input().split())
A = (list(map(int,input().split())))
B = (list(map(int,input().split())))


A.sort(reverse=True)
B.sort(reverse=True)

def binary_serch(d):
    l = -1
    r = m
    while(r-l > 1):
        mid = (l+r)//2
        if B[mid] >= d:
            l = mid
        else:
            r = mid

    return mid

for i in A:
    if (binary_serch(i-d))
