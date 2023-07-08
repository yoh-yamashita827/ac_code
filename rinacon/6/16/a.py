a,b = map(int,input().split())

max = 2*a+100

if max-b < 0:
    print(0)
print(max-b)