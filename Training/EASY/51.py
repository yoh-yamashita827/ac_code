n,a,b = map(int,input().split())
cnt = 0
for i in range(1,n+1):
    tmp = 0
    for j in str(i):
        tmp += int(j)
    
    if a <= tmp <= b:
        cnt += i
        # print(i)
print(cnt)