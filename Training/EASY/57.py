a,b = map(int,input().split())

for i in range(13,1251):
    if int(i*0.08) == a:
        if int(i*0.1) == b:
            print(i)
            exit()

print(-1)