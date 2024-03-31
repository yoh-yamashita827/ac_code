x1,y1,x2,y2 = map(int,input().split())

dx = (x1-x2)
dy = (y1-y2)

x3 = x2+dy
y3 = y2-dx

x4 = x3+dx
y4 = y3+dy

print(x3,y3,x4,y4)