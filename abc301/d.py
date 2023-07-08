S = (input())
N = int(input())


s_max = S.replace('?','1')
s_min = S.replace('?','0')

if not (int(s_min,2) <= N):
    print(-1)
    exit()

if N >= int(s_max,2):
    print(int(s_max,2))
    exit()

## n -> 2進
n_2 = format(N,'0'+str(len(S))+'b')
ls1 = n_2.rfind('1')


# ans = ''
tmp = list(S)
ans = list(S)
for i,v in enumerate(S):
    if v != '?':
        ans[i] = str(v)
    
    else:
        tmp[i] = '1'
        tmp = ''.join(tmp).replace('?','0')
        if int(tmp,2) <= N:
            ans[i] = '1'

        else: ans[i] = '0'
        tmp = ans


print(int(''.join(ans),2))





