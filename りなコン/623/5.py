k,n = map(int,input().split())
A = list(map(int,input().split()))
B = []

min_d = 10000000000
id = 0
for i in range(len(A)-1):
    now = A[i]
    next = A[i+1]

    B.append(next-now)


B.append(A[0]+(k-A[-1]))
print(sum(B)-max(B))
    






