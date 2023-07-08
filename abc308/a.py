S = list(map(int,input().split()))
pre = 0
for i in S:
    if pre > i:
        print('No')
        exit()
    if i%25 != 0:
        print('No')
        exit()
    if (100 > i) or (i > 675):
        print('No')
        exit()
    pre = i

print('Yes')