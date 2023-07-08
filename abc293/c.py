# from collections import deque
# h,w = map(int,input().split())
# A = []
# for _ in range(w):
#     A.append(list(map(int,input().split())))

# import itertools
# right = 'R'*(w-1)
# down = 'D'*(h-1)

# from itertools import permutations
# st = set()
# l = []
# for it in permutations(right+down):
#     st.add("".join(it))
#     l.append("".join(it))
# # print(sorted(st))
# # print(sorted(l))


# dx = [1,0]
# dy = [0,1]
# R = 0
# D = 1
# cnt = 0

# for i in st:
#     num = set()
#     x = y = 0
#     num.add(A[x][y])
#     for j in i:
#         if j == 'R':
#             x += dx[R]
#             y+= dy[R]
#         else:
#             x += dx[D]
#             y += dy[D]
#         if A[x][y] not in num:
#             num.add(A[x][y])
#             if len(num) == len(i)+1:
#                 cnt += 1
#         else:
#             break

# print(cnt)
        
from sys import stdin
H, W = map(int, input().split())
A = [list(map(int, stdin.readline().split())) for _ in range(H)]

count = 0

# bit全探索
for i in range(2 ** (H + W - 2)):
    y, x = 0, 0
    S = {A[y][x]}

    for j in range(H + W - 2):
        if (i >> j) & 1:
            y += 1
            if y == H:
                break
        else:
            x += 1
            if x == W:
                break
        S.add(A[y][x])

    if len(S) == H + W - 1:
        count += 1

print(count)

