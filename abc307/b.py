n = int(input())
S = []
for _ in range(n):S.append(input())
flg = True
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        plas = S[i]+S[j]

        for m in range(len(plas)):
            if plas[m] != plas[len(plas)-1-m]:
                flg = False

        if flg:
            print('Yes')
            exit()

        flg = True

print('No')