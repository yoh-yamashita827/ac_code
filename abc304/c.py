n,d = map(int,input().split())

xy = []
ans = ['No']*n
for i in range(n):
    xy.append(list(map(int,input().split())))

def eq(a1,a2,b1,b2):
    return ((a1-b1)**2)+((a2-b2)**2)

# ans[0] = 'Yes'
# for i in range(n):
#     for j in range(n):
#         now = xy[i]
#         next = xy[j]

#         if eq(now[0],now[1],next[0],next[1]) <= (d**2):
#             if ans[i] == 'Yes':

#                 ans[j] = 'Yes'


# for i in ans:
#     print(i)

import sys
sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限
dye = set()
def dfs(now):
    dye.add(now)

    for i in range(n):
        if i in dye:
            continue
        if eq(xy[now][0],xy[now][1],xy[i][0],xy[i][1]) <= (d**2):
            dfs(i)

    
    

dfs(0)

for i in range(n):
    if i in dye:
        print('Yes')
    else:
        print('No')
