N = int(input())
cnt = 0


for c in reversed(range(1,N+1)):
    for b in range(1, (N//c)+1):
        if c < b:
            break
        for a in range(1, (N//(b*c))+1):
            if  b < a :
                break
            if  a*b*c <= N:
                cnt += 1

print(cnt)

