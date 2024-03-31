a,b,c=map(int,input().split())
d = e = f = 0
if a==b==c==1:
    print(0)
if a==b==c:
  print(-1)
  exit()
tmp=[i%2 for i in [a,b,c]]
if 1 in tmp:
  print(0)
  exit()
cnt=0
while d%2 == e%2 == f%2 ==  0 :
    d=(b+c)/2
    e=(a+c)/2
    f=(b+a)/2
    a=d
    b=e
    c=f
    cnt += 1

print(cnt)


