import statistics
n = int(input())
# ori_x = []
# ori_y = []
x = []
y = []
xy = set()
for _ in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
    xy.add((a,b))

# for i in xy:
#     x.append(i[0])
#     y.append(i[1])
x.sort()
y.sort()
mid_x = statistics.median(x)
mid_y = statistics.median(y)

ans = 0
for i,j in zip(x,y):
    ans += (abs(i-mid_x)+ abs(j-mid_y))

print(int(ans))



