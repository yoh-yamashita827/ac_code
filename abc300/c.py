import numpy as np
h,w = map(int,input().split())
c = [list(map(str,list(input()))) for i in range(h)]
ans = [0]*min(h,w)

#serach
for i in range(1,h-1):
    for j in range(1,w-1):
        d = 1
        now = c[i][j]
        if now == '#':
            tmp = []
            r = min(i,h-i-1,j,w-j-1)
            while(d<=r):
                if not(c[i+d][j+d] == c[i+d][j-d] == c[i-d][j+d] == c[i-d][j-d] == '#'):
                    break
                else:
                    tmp.append(d)
                    d += 1
            if tmp ==  []:
                continue
            ans[tmp[-1]-1] += 1
            


print(*ans)