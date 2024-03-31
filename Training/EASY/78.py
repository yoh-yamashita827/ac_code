n = int(input())
h = list(map(int,input().split()))

pre = 0
for i in h:
    if i-pre > 0:
        pre = i-1
    elif i==pre:
        pre = i

    else:
        print('No')
        exit()

print('Yes')