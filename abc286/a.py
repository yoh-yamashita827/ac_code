N,P,Q,R,S = map(int,input().split())
A = list(map(int,input().split()))
# S = []
# for _ in range(N):
#    S.append(input())

pq = A[P-1:Q]
rs = A[R-1:S]

A[R-1:S] = pq
A[P-1:Q] = rs

print(*A)