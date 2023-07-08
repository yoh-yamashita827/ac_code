S,T,X = map(int,input().split())
list = []
c = T - S
if c < 0:
    c += 24

for _ in range(c):
    list.append(S)
    S += 1
    if  S == 24:
        S = 0

if  X in list:
    print('Yes')
else:
    print('No')