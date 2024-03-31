# n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
import numpy as np
P1 = []
P2 = []
P3 = []

for _ in range(4):
    P1.append(list(input()))

for _ in range(4):
    P2.append(list(input()))

for _ in range(4):
    P3.append(list(input()))

ans  = 0

def make_pattern(P):
    pattern = []
    cnt = sum(sum(P=='#'))

    for _ in range(4):
        P = P[::-1].T
        map = np.array([['.']*7 for _ in range(7)])
        for i in range(4):
            for j in range(4):
                map[i][j] = P[i][j]


        for i in range(4):
            for j in range(4):
                tmp = (map[i:i+4,j:j+4])
                if sum(sum(tmp=='#')) == cnt:
                    pattern.append(tmp)


    return (pattern)


pt1 = make_pattern(np.array(P1))
pt2 = make_pattern(np.array(P2))
pt3 = make_pattern(np.array(P3))


for i in pt1:
    for j in pt2:
        for k in pt3:
            map = np.array([['.']*4 for _ in range(4)])
            # map = k

            # for k2 in range(4):
            #     for kk2 in range(4):

            for j2 in range(4):
                for jj2 in range(4):
                    if map[j2][jj2] == j[j2][jj2] == '#':
                        break
                    elif j[j2][jj2] == '#':   
                        map[j2][jj2] = j[j2][jj2]

            for i2 in range(4):
                for ii2 in range(4):
                    if map[i2][ii2] == i[i2][ii2] == '#':
                        break
                    elif j[j2][jj2] == '#':   
                        map[i2][ii2] == i[i2][ii2]
            
            if sum(sum(map=='#')) == 16:
                print('Yes')
                exit()

print('No')