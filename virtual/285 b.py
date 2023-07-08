N = int(input())
S = list(input())
ans = []

for i in range(1,N):
    j = 0
    while(j+i < N):
        now = S[j]
        next = S[j+i]

        if now == next:
            break
        j+=1
    print(j)
