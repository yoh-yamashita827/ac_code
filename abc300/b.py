H,W = map(int,input().split())
A = []
B = []
for i in range(H):
    A.append(list(input()))
for i in range(H):
    B.append(list(input()))
flg = False
def dot_count(ori):
    import numpy as np
    dot = 0
    yoko = []
    tate = []
    for i in ori:
        tmp = i.count('.')
        dot += tmp
        yoko.append(tmp)
    
    transpose = np.array(ori).T
    for i in transpose:
        tate.append(list(i).count('.'))

    return dot,yoko,tate

a_dot,a_yoko,a_tate = dot_count(A)
b_dot,b_yoko,b_tate = dot_count(B)

if a_dot != b_dot:
    print('No')
    exit()

for i in range(H):
    if a_yoko == b_yoko:
        flg = True
        break
    a = a_yoko.pop(0)
    a_yoko.append(a)

if flg:
    for i in range(W):
        if a_tate == b_tate:
            print('Yes')
            exit()
        a = a_tate.pop(0)
        a_tate.append(a)

print('No')




