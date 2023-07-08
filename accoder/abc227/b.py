N = int(input())
l = list(map(int, input().split()))
n = N


for i in l:
    for a in range(350):
        for b in range(350):
            if  4*a*b+3*a + 3*b == i:
                N -= 1
                break
        else:
            continue
        break    
        


    

print(N)
