import numpy as np

HA,WA = map(int,input().split())
A = []
for _ in range(HA):
    A.append(list(input()))

HB,WB = map(int,input().split())
B = []
for _ in range(HB):
    B.append(list(input()))

HX,WX = map(int,input().split())
X = []
for _ in range(HX):
    X.append(list(input()))

A = np.array(A)
B = np.array(B)
X = np.array(X)
C = np.array([['.']*(WA+WB) for _ in range(HA+HB)])

for ha in range(HB):
    for wa in range(WB):
        for hb in range(HA):
            for wb in range(WA):
                map = C.copy()
                map[ha:ha+HA,wa:wa+WA] = A
                map[hb:hb+HB,wb:wb+WB] = B

                if sum(sum(map=='#')) != sum(sum(X=='#')):
                    continue
                for k in range(HA+HB):
                    for l in range(WA+WB):
                        if np.array_equal(X,map[k:k+HX,l:l+WX]):
                            print('Yes')
                            exit()
print('No')
