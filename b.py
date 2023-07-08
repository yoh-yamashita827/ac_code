import math
from unittest import skip
N, K = map(int,input().split())
A = list(map(lambda x:x-1,  list(map(int,input().split()))))

A = set(A)
XY = []
# print(A)
for _ in range(N):
    x, y = map(int, input().split())
    XY.append([x, y])
# max_dist = 0
# ans = float("inf")
ans = 0

for j in range(N):

    min_dist = float("inf")
    for i in range(N):
        if i not in A:
            continue
        dist = math.sqrt((XY[j][0]-XY[i][0])**2+(XY[j][1]-XY[i][1])**2)
        # print(d)
        if dist < min_dist:
            min_dist = dist
    # print(max_dist)
    if min_dist  > ans:
        ans = min_dist

print(ans)


