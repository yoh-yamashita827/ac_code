S = list(str(input()))
s = len(S)
flg = False
T = []
i = 0

if s == 1:
    if (S == ['o']) or (S == ['x']):
        flg = True

if s == 2:
    if (S == ['o','x']) or (S == ['x','o']) or (S == ['x','x']):
        flg = True


if s >= 3:
    if (S[:3] == ['o','x','x']) or (S[:3] == ['x','x','o']) or (S[:3] ==['x','o','x']):
        flg = True


for _ in range(s):
    if i > 3:
        i -= 3

    T.append(S[i])
    i += 1

print(S[:3],T,s)
if flg and T == S:
    print('Yes')
else:
    print('No')



