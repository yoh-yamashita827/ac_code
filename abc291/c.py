n = int(input())
s = input()

dx = [1,-1,0,0]
dy = [0,0,1,-1]
R,L,U,D = 0,1,2,3

visited = set()

x,y = 0,0
visited.add((x,y))
for i in s:
    if i == 'R':
        x += dx[R]
        y += dy[R]    
    elif i == 'L':
        x += dx[L]
        y += dy[L]    
    elif i == 'U':
        x += dx[U]
        y += dy[U]    
    elif i == 'D':
        x += dx[D]
        y += dy[D]
    if not (x,y) in visited:
        visited.add((x,y))
    else:
        print('Yes')
        exit()

print('No')


