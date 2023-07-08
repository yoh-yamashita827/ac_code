n,m = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort(reverse = True)
B = B[::-1]

print(A,B)

ans = 0
# for b in reversed(B):
#     for a in A:
#         if a <= b:
#             ans += 1
#             A.pop()
a = 0
b = 0

while((a != n)and(b != m)):
    if A[a] <= B[b]:
        a += 1
        b += 1
        ans += 1
    else:
        a += 1


print(ans)