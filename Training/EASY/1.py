a,b=map(int,input().split())
if b == 1:
    print(0)
    exit()
cnt = 0
i = 0
while(cnt<b):
    if cnt == 0:
        cnt += a

    else:
        cnt += (a-1)

    i += 1
print(i)