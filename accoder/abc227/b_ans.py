N = int(input())
l = list(map(int, input().split()))
cnt = 0


for i in l:
    flag = False
    for a in range(350):
        for b in range(350):
            if  4*a*b + 3*a + 3*b == i:
                flag = True
                break
    if not flag:
        cnt += 1  
        

print(cnt)