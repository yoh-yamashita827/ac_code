n = int(input())

S = list(str(n))
s = 0
for i in S:
    s += int(i)

if n%s == 0:
    print('Yes')
else:
    print('No')