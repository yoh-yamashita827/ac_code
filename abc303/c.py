n,m,h,k = map(int,input().split())
S = input()
item = set()
for i in range(m):
    item.add(tuple(map(int,input().split())))

used = set()

def move(x,y,d):
    if d == 'R':
        return x+1,y
    elif d == 'L':
        return x-1,y
    elif d == 'U':
        return x,y+1    
    elif d == 'D':
        return x,y-1
x = y = 0
for i in S:
    x,y = move(x,y,i)
    h -= 1

    if h < 0:
        print('No')
        exit()

    if (x,y) not in item:
        continue
    if (x,y) in used:
        continue
    if h < k:
        h = k
        used.add((x,y))

print('Yes')


