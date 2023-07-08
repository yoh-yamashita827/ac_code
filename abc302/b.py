h,w = map(int,input().split())

S = []
for i in range(h):
    S.append(list(input()))
SS = []
for i in range(h):
    SS.append(S[i][::-1])

def check(a,b,c,d,e):
    if (a == 's')and(b == 'n')and(c == 'u')and(d == 'k')and(e == 'e'):
        return 1
    elif (e == 's')and(d == 'n')and(c == 'u')and(b == 'k')and(a == 'e'):
        return 2
    return 0


for i in range(h):
    for j in range(w-4):

        a,b,c,d,e = S[i][j],S[i][j+1],S[i][j+2],S[i][j+3],S[i][j+4]
        if check(a,b,c,d,e) == 1:
            for k in range(5):
                print(i+1,j+k+1)
            exit()
        if check(a,b,c,d,e) == 2:
            for k in range(5):
                print(i+1,j+5-k)
            exit()


for i in range(h-4):
    for j in range(w):

        a,b,c,d,e = S[i][j],S[i+1][j],S[i+2][j],S[i+3][j],S[i+4][j]
        if check(a,b,c,d,e) == 1:
            for k in range(5):
                print(i+k+1,j+1)
            exit()
        if check(a,b,c,d,e) == 2:
            for k in range(5):
                print(i+4-k+1,j+1)
            exit()

for i in range(h-4):
    for j in range(w-4):
        a,b,c,d,e = S[i][j],S[i+1][j+1],S[i+2][j+2],S[i+3][j+3],S[i+4][j+4]

        if check(a,b,c,d,e) == 1:
            for k in range(5):
                print(i+k+1,j+k+1)
            exit() 
        if check(a,b,c,d,e) == 2:
            for k in range(5):
                print(i+4-k+1,j+4-k+1)
            exit() 

        a,b,c,d,e = SS[i][j],SS[i+1][j+1],SS[i+2][j+2],SS[i+3][j+3],SS[i+4][j+4]   

        if check(a,b,c,d,e) == 1:
            for k in range(5):
                print(i+k+1,w-j-k)
            exit()         
        if check(a,b,c,d,e) == 2:
            for k in range(5):
                print(i-k+4+1,w-j-4+k)
            exit()         
