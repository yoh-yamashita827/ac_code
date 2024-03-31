q,h,s,d = map(int,input().split())
n = int(input())

h = min(h,q*2)
s = min(s,h*2)
d = min(d,s*2)

if n%2 == 0:
    print(d*(n//2))
else:
    print((d*(n//2))+s)