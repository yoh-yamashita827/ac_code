import bisect as bi


n,q = map(int,input().split())
LR = []

for i in range(n):
    l,r = map(int,input().split())
    LR.append((l,r))


# ans = []
prt = []
for _ in range(q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        LR[query[1]] = (query[2],query[3])
        
    else:
        LI = []
        ans = 0
        k = query[1]
        for i in range(n):
            LI.append([LR[i][0],i])
        LI.sort()

        for i in range(n):
            cnt = 0
            for j in LI:
                if LR[i][1] > j[0]:
                    cnt += 1
                elif LR[i][1] == j[0]:
                    if i <= j[1]:
                        cnt += 1
            # print(i,cnt)
            if n-cnt+1 <= k:
                ans += 1
        prt.append(ans)

            # indl = bi.bisect_left(LI,[LR[i][1],-i])
            # indr = bi.bisect_right(LI,[LR[i][1],-i])
            # prt.append((indl, indr))
            # ans.append(indl)

            # if n-indr <=k:
            #     ans +=1

            # if n-(indl-1) <= query[1]:
            #     ans.append(n-(indl-1))
            #     # print(n-(indl-1))

            # if indl != indr:
            #     cnt = 0
            #     for j in range(indl,indr):
            #         if LI[j][1] < (-i):
            #             cnt += 1

            #     print(indl+cnt)
        # prt.append(ans)
for i in prt:
    print(i)