n,m = map(int,input().split())
ll = -100000000
rr = 100000000

for i in range(m):
    l,r = map(int,input().split())

    ll = max(ll,l)
    rr = min(rr,r)
    
print(len(list(range(ll,rr+1))))