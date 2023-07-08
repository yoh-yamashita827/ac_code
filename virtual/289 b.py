N,M = map(int,input().split())
a = list(map(int,input().split()))
nums = [i for i in range(1,N+1)]
c = []
if M == 0:
    print(*range(1,N+1))
    exit()

tmp = []
for i in nums:

    tmp.append(i)
    if i  not in a:
        c.extend(tmp[::-1])
        tmp = []
    
print(*c)
    