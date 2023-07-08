N,M = map(int,input().split())
B = [list(map(int,input().split())) for l in range(N)]


for i in range(N):
    for j in range(M):
        if B[i][j] %7 == 0:
            if B[i][j] != B[i][M-1]:
             print('No')
             exit(0)

for i in range(N-1):
    for j in range(M):
        if (B[i+1][j] - B[i][j] != 7):
            print('No')
            exit(0)
            
    
for i in range(N):
    for j in range(M-1):
        if B[i][j+1] - B[i][j] != 1:
            print('No')
            exit(0)

print('Yes')


