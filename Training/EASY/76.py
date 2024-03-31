n,m = map(int,input().split())
AC = {}
WA = 0

def return_num(x):
    if x == 'AC':
        return 1
    else:
        return 0

for _ in range(m):
    p,s = map(str,input().split())
    S = return_num(s)
    if p not in AC.keys():
        AC[p] = [S]
    else:
        AC[p].append(S)

ans_que = {i:v for i,v in AC.items() if 1 in v}

ans = 0

for i in ans_que.values():
    for j in i:
        if j == 0:
            WA += 1
        else:
            ans += 1
            break

print(ans,WA)