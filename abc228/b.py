N, X = map(int,input().split())
A = list(map(int,input().split()))
list = []
list.append(X)
# list.append(A[X-1]) 

for i in range(N+1):
    list.append(A[list[i]-1])

print(len(set(list)))