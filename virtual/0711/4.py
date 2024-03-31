n,m = map(int,input().split())
AB = []


for _ in range(n):
    a,b = map(int,input().split())
    AB.append([a,b])


cheper = sorted(AB,key= lambda x:x[0])

cnt = 0
price = 0
for i in cheper:
    if cnt + i[1] <= m:
        cnt += i[1]
        price += i[0]*i[1]
    else:
        tmp = m-cnt
        cnt += tmp
        price += tmp*i[0]

print(price)


