
n = int(input())
A = list(map(int,input().split()))
v = 0
visit = set()
while(v not in visit):
    visit.add(v)
    v = A[v]-1

roop = set()
while(v not in roop):
    roop.add(v)
    v = A[v]-1

print(len(roop))

ans = []
ans.append(v+1)
while(len(ans) != len(roop)):
    ans.append(A[v])
    v = A[v]-1

    
print(*ans)





    
    
