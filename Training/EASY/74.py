a,b,c,x,y = map(int,input().split())

ans1 = (a*x)+(b*y)

if x >= y:
    sub = (x-y)
    ans2 = (2*y*c)+(sub*a)

else:
    sub = (y-x)
    ans2 = (2*c*x)+(sub*b)

ans3 = (2*c*max(x,y))

print(min(ans1,ans2,ans3))