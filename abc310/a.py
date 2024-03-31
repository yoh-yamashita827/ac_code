n,p,q = map(int,input().split())
D = list(map(int,input().split()))

w = q + min(D)

print(min(p,w))