import math
N = int(input())
c = math.factorial(N) // (math.factorial(N - 3) * math.factorial(3))

l = []
strate = []
cnt = 0

for i in range(N):
    x,y = input().split()
    l.append([int(x),int(y)])

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if (l[i][0])*(l[j][1]) - (l[j][0])*(l[i][1]) == 0:
                if  (l[i][0])*(l[k][1]) - (l[k][0])*(l[i][1]) == 0:
                    if (l[j][0])*(l[k][1]) - (l[k][0])*(l[j][1]) == 0:
                        print(i,j,k)
                        cnt += 1
            
print(cnt)    

