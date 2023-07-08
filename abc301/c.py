S = list(input())
T = list(input())
a = list('atcoder')
SS = S.copy()
TT = T.copy()

for i in range(len(S)):
    if S[i] in a:
        SS[i] = '@'
    if T[i] in a:
        TT[i] = '@'

s = list(set(SS))
t = list(set(TT))
for j in range(len(s)):
    if (SS.count(s[j]) != TT.count(s[j])):
        print('No')
        exit()
    if (SS.count(t[j]) != TT.count(t[j])):
        print('No')
        exit()        
    if (s[j] not in t):
        print('No')
        exit()
    if t[j] not in s:
        print('No')
        exit()

ta = 0
sa = 0
for k in a:
    tmp= ((S.count(k))-T.count(k))
    if tmp > 0:
        sa += tmp
    else:
        ta += -(tmp)

if T.count('@')-sa >= 0:
    if S.count('@')-ta >= 0:
        print('Yes')
else:
    print('No')

# dif += ((S.count('@'))-T.count('@'))

# if (dif < 0):
#     print('No')
#     exit()


