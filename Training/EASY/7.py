A = [list(map(int,input().split())) for _ in range(3)]
n = int(input())

def panch(x):
    for i in range(3):
        for j in range(3):
            if A[i][j]==x:
                return i,j
    return -1,-1

for _ in range(n):
    b = int(input())
    i,j = panch(b)
    if i!=-1:
        A[i][j]=0



for i in A:
    if sum(i)==0:
        print('Yes')
        exit()

if (A[0][0]+A[1][1]+A[2][2]==0)or(A[0][2]+A[1][1]+A[2][0]==0):
    print('Yes')
    exit()

A = list(zip(*A))
for i in A:
    if sum(i)==0:
        print('Yes')
        exit()
print('No')


    