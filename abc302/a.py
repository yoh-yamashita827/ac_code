a,b = map(int,input().split())
if a%b ==0:
    print(int(a//b))
    exit()
print(int(a//b)+1)