n,q = map(int,input().split())
carded = {}
for _ in range(q):
    ques = list(map(int,input().split()))

    if ques[0] == 1:
        if ques[1] not in carded:
            carded[ques[1]] = 1
        else:
            carded[ques[1]] = 2

    elif ques[0] == 2:
        carded[ques[1]] = 2

    else:
        if ques[1] not in carded:
            print('No')
            continue

        if carded[ques[1]] == 2:
            print('Yes')
        else:
            print('No')
