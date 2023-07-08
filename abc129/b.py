N = int(input())
W = list(map(int,input().split()))
a = 0
b = 0
min = 100

for i in range(1,N):
    for j in range(i):
        a += W[j]
        
    for k  in range(i,N):
        b += W[k]
    
    y = abs(a-b)
    
    a,b = 0,0
    if min > y:
        min = y

print(min)