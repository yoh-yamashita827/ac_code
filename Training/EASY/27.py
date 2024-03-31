n,a,b = map(int,input().split())

m = n%(a+b)
r = n//(a+b)

if m <= a:
    print((a*r)+m)
else:
    print((a*r)+a)