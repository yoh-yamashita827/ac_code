n = 8
s = []
for i,v in enumerate(range(n)):
    tmp = list(input())
    if '*' in tmp:
        loc = i
    s.append(tmp)

for j in range(8):
    if s[loc][j] == '*':
        x,y = j,loc

xx = ['a','b','c','d','e','f','g','h']
yy = range(1,n+1)
yy = yy[::-1]
yy = [str(i) for i in yy]

print(xx[x]+yy[y])
