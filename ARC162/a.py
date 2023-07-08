T = int(input())

for i in range(T):
    N = int(input())
    P = (list(map(int,input().split())))
    exist = set()
    cnt = 0
    for i in range(N):
        if P[i] == N:
            break
        exist.add(P[i])
        if i+1 in exist:
            cnt += 1

    print(cnt) 

# changed = {}
# for i,v in enumerate(P):
#     d = v-(i+1)
#     if d >= 0:
#         changed[v] = d


