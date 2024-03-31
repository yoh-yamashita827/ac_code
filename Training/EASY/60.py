n = int(input())
t = list(map(int,input().split()))
m = int(input())
base = sum(t)
for _ in range(m):
    p,x = map(int,input().split())
    print(base-(t[p-1]-x))
