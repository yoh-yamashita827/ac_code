import numpy as np
N = int(input())
A = []
for _ in range(N):
    A.append(list(input()))

tmp = []
map = np.array(A)
for i in range(4):
    tmp.extend(map[0])
    tmp.pop()
    map = map.T[::-1]


next = [tmp.pop()]+ tmp


ans = np.array([[0]*N for _ in range(N)])

for i in range(4):
    ans[0][0:N-1] = next[i*(N-1):i*(N-1)+N-1]
    ans = ans.T[::-1]




for i in range(N):
    for j in range(N):
        if (i == 0) or (i == N-1) or (j == 0) or (j == N-1):
            continue

        ans[i][j] = A[i][j]

for a in ans.tolist():
    mm = [str(v) for v in a ]
    print(''.join(mm))