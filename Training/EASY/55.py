n,d = map(int,input().split())
x = [list(map(int,input().split())) for _ in range(n)]
import itertools
cnt = 0
for i in itertools.combinations(range(n),2):
    tmp = 0
    x1 = x[i[0]]
    x2 = x[i[1]]

    for j in range(d):
        tmp += (x1[j]-x2[j])**2

    if tmp == (int(tmp**(1/2)))**2:
        cnt += 1

print(cnt)