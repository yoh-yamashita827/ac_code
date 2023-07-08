a,b,x,y = map(int,input().split())

if abs(x-a) > 4 or abs(y-b) > 4:
    print('No')
    exit(0)

ab_lis = []
xy_lis = []

ab_lis.append([a+2,b+1])
ab_lis.append([a+2,b-1])
ab_lis.append([a+1,b+2])
ab_lis.append([a+1,b-2])
ab_lis.append([a-1,b+2])
ab_lis.append([a-1,b-2])
ab_lis.append([a-2,b+1])
ab_lis.append([a-2,b-1])

xy_lis.append([x+2,y+1])
xy_lis.append([x+2,y-1])
xy_lis.append([x+1,y+2])
xy_lis.append([x+1,y-2])
xy_lis.append([x-1,y+2])
xy_lis.append([x-1,y-2])
xy_lis.append([x-2,y+1])
xy_lis.append([x-2,y-1])


for i in range(8):
    for j in range(8):
        if ab_lis[i] == xy_lis[j]:
            print('Yes')
            exit(0)

print('No')