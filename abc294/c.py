n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
a=b=0
a_id =[]
b_id = []
while ((b < len(B))and(a < len(A))):
    if A[a]-B[b] < 0:
        a_id.append(a+b+1)
        a += 1
    else:
        b_id.append(a+b+1)
        b += 1

if a == len(A):
    b_id.extend(range(a+b+1,len(A+B)+1))
else:
    a_id.extend(range(a+b+1,len(A+B)+1))

print(*a_id)
print(*b_id)