n = int(input())
memo  = {}
tmp = {}

tmp[1] = 0
tmp[2] = 0

memo[0] = tmp

for i in range(1,n+1):
    tmp = tmp.copy()
    c,p = map(int,input().split())
    # if c == 1:
    #     tmp[1] = memo[i-1][1] + p
    #     tmp[2] = memo[i-1][2]
    # else:
    #     tmp[1] = memo[i-1][1] 
    #     tmp[2] = memo[i-1][2] + p      
    tmp[c] += p
    memo[i] = tmp

q = int(input())
for i in range(q):
    l,r = map(int,input().split())
    print(memo[r][1]-memo[l-1][1],memo[r][2]-memo[l-1][2])
    
    
    