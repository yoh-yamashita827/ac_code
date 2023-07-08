import itertools

n,m = map(int,input().split())
S = [list(input()) for i in range(n)]
T = S.copy()
def check(now,next):
    now = now.copy()
    next = next.copy()
    now.sort()
    next.sort()
    # if now == next:
    #     return 0

    for i in range(len(now)):
        if now[i] in next:
            next.remove(now[i])
    if len(next) == 1:
        return 1
    else:
        return 0
    
def diff(now,next):
    res = 0
    for a, b in zip(now, next):
        if a != b:
            res += 1
    return res

for i in itertools.permutations(S):
    flg = True

    for j in range(len(i)-1):
        # if not check(i[j],i[j+1]):
        #     flg = False
        #     # break
        if diff(i[j],i[j+1]) != 1:
            flg = False
                  
    if flg:
        print('Yes')
        exit()

print('No')

