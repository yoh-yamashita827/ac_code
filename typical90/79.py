import numpy as np
h,w = map(int,input().split())

A = []
B = []

for _ in range(h):
    A.append(list(map(int,input().split())))

for _ in range(h):
    B.append(list(map(int,input().split())))


delta = [[0] * w for i in range(h)]
cnt = 0
for i in range(h):
    for j in range(w):
        delta[i][j] = B[i][j]-A[i][j]
        cnt += B[i][j]-A[i][j]

if cnt % 4 != 0:
    print('No')
    exit()

ans = 0
delta = np.array(delta)

for i in range(w-1):
    for j in range(h-1):
        window = delta[h-(j+2):h-j,i:i+2]
        ans += abs(window[1][0])
        window -= window[1][0]

print('Yes')
print(ans)
