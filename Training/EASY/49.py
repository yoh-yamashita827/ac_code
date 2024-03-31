h,w = map(int,input().split())
maps = [['#']*(w+2) for _ in range(h+2)]
a = [input() for _ in range(h)]
for i,v in enumerate(maps):
    if (i == 0) or (i == h+1):
        continue
    else:
        v[1:w+1] = a[i-1]

for i in maps:
    print(''.join(i))