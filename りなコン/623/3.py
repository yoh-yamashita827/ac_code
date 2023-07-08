n = int(input())
t = input()

dxy = [[1,0],[0,-1],[-1,0],[0,1]]

x = y = 0
id = 0
for i in t:
    if i == 'S':
        x += dxy[id][0]
        y += dxy[id][1]
    else:
        id += 1
        id = id%4

print(x,y)