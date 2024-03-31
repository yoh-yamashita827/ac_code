n = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
a = 0
b = 0
for i,v in enumerate(A):
    if i%2 == 0:
        a += v
    else:
        b += v

print(a-b)
