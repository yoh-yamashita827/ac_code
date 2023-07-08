import sys
sys.setrecursionlimit(10**9)
H,W = map(int,input().split())
S = []
for _ in range(H):
    S.append(input())

T = ['s','n','u','k','e']
# xy = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]

# for i in range(H):
#     for j in range(W):
# def expand(na,nb): 
#     tmp = []
#     for i,j in xy:

#         if (0 <= na+i < W) and (0 <= nb+j < H):
#             tmp.append([na+i,nb+j])

#     return tmp

visit = set()
def dfs(a,b,t):
    if (a,b) in visit:
        return
    t = t%5
    if not(0 <= a < W) or not(0 <= b < H):
        visit.add((a,b))
        return 
    if S[b][a] != T[(t)%5]:
        return


    if (b,a) == (H-1,W-1):
        print('Yes')
        sys.exit()
    
    dfs(a-1,b-1,t+1)
    dfs(a,b-1,t+1)
    dfs(a+1,b-1,t+1)
    dfs(a-1,b,t+1)
    dfs(a+1,b,t+1)
    dfs(a-1,b+1,t+1)
    dfs(a,b+1,t+1)
    dfs(a+1,b+1,t+1) 


dfs(0,0,0)
print('No')