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
        LR[i] = (query[2],query[1])
        
    else:
        LI = []
        ans = 0
        k = query[1]
        for i in range(n):
            LI.append([LR[i][0],-i])
        LI.sort()

        for i in range(n):
            l = 0
            r = n
            while r-l>1:
                mid = r+l
                mid //=2

                if LI[mid][0] <= LR[i][1]:
                    r = mid

                else:
                    l = mid + 1

            indl = l

            l = 0
            r = n
            while r-l>1:
                mid = r+l
                mid //=2

                if LI[mid][0] < LR[i][1]:
                    r = mid

                else:
                    l = mid + 1
            
            indr = l

            # indl = bi.bisect_left(LI,[LR[i][1],-i])
            # indr = bi.bisect_right(LI,[LR[i][1],-i])
            prt.append((indl, indr))
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