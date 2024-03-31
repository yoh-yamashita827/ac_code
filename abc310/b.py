n,m = map(int,input().split())

P = []
for _ in range(n):
    P.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        Pi = P[i][0]
        Ci = P[i][1]
        Fi = P[i][2:]
        
        Pj = P[j][0]
        Cj = P[j][1]
        Fj = P[j][2:]

        if Pi >= Pj:
            if (set(Fi)<=set(Fj)):
                if (Pi > Pj) or (Ci < Cj):
                    print('Yes')
                    exit()


        # if Pi > Pj:
        #     if Ci < Cj:
        #         if (set(Fi)<=set(Fj)):
        #             exit()

        
print('No')