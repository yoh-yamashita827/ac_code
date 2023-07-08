n = int(input())
ab = []
for _ in range(n):
    ab.append(list(map(int,input().split())))

X = 998244353

case = set()
# b = set()
count = {}
for i in range(3):
    count[i] = 0
ans = 0
for i in ab:
    cnt = 0
    if not i[0] in case:
        case.add(i[0])
        cnt += 1

    if not i[1] in case:
        case.add(i[1])
        cnt += 1

    count[cnt] += 1
import math 
print(((2**count[2])*(math.factorial(count[1]))%X))


    



