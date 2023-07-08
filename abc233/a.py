x,y = map(int,input().split())
cnt = 0

for i in range(1000):
    if x < y:
        x += 10
        cnt +=1

print(cnt)

