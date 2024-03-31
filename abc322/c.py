# n = int(input())
n,m = map(int,input().split())
# s = input()
a = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

def binary(A,x):
    l = 0
    r = len(A)

    while(r!=l):
        m = (r+l)//2
        if A[m] >= x:
            r = m
        else:
            l = m+1    
    return r 

for i in range(1,n+1):
    tmp = binary(a,i)
    print(a[tmp]-i)