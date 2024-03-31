from collections import defaultdict

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

mod = 46

A = [i%mod for i in A]
B = [i%mod for i in B]
C = [i%mod for i in C]

a = defaultdict(int)
b = defaultdict(int)
c = defaultdict(int)

for i in A:
    a[i] += 1

for i in B:
    b[i] += 1

for i in C:
    c[i] += 1

ans = 0
for i in a.keys():
    for j in b.keys():
        for k in c.keys():
            if (i+j+k)%46 == 0:
                ans += (a[i]*b[j]*c[k])

print(ans)