n = int(input())
# n,m = map(int,input().split())
# s = input()
A = list(map(int,input().split()))
# s = []
# for _ in range(n):
#    s.append(input())

A.sort()

pre = A[0]
for i in range(1,n):
    if A[i]-pre != 1:
        print(A[i]-1)
        exit()
    pre = A[i]

    