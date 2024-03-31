n = int(input())
p = list(map(int,input().split()))

cnt = 0
mmm = p[0]

for i in p:
    if mmm >= i:
        cnt += 1

    mmm = min(mmm,i)

print(cnt) 