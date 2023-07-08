N, T = map(int,input().split())
C = list(map(int,input().split()))
R = list(map(int,input().split()))

a = 0
inds = [i for i, x in enumerate(C) if x == T]
if inds != []:
    for i in inds:
        num = R[i]
        if a < num:
            a = num
    print(R.index(a)+1)

else:
    inds = [i for i, x in enumerate(C) if x == C[0]]
    for i in inds:
        num = R[i]
        if a < num:
            a = num
    print(R.index(a)+1)