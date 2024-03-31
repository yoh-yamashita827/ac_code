N,Q=map(int,input().split())
A=list(map(int,input().split()))
B=[0]*(N-1)
f=0
ans=[]
for i in range(N-1):
    B[i]=A[i]-A[i+1]
    f+=abs(B[i])
for i in range(Q):
    l,r,v=map(int,input().split())
    l-=1
    r-=1
    if l!=0:
        f-=abs(B[l-1])
        B[l-1]-=v
        f+=abs(B[l-1])
    if r!=N-1:
        f-=abs(B[r])
        B[r]+=v
        f+=abs(B[r])
    
    ans.append(f)
for a in ans:
    print(a)