N = int(input())
Q = int(input())
B = {}
number = {}

qs = [list(map(int,input().split())) for _ in range(Q)]
# req = list(set([i[1] for i in qs if len(i)==2]))
tokkan = set()

import bisect
for i in range(Q):
    # q = list(map(int,input().split()))
    q = qs[i]
    # if (len(q)==3)and(q[2] not in req):
    #     continue
    if q[0] == 1:
        # B[q[2]].append(q[1])
        # number.setdefault(q[1],[]).append(q[2])
        if q[2] not in B:
            B[q[2]] = []
        bisect.insort(B[q[2]],q[1])

        if (q[1], q[2]) not in tokkan:
            if q[1] not in number:
                number[q[1]] =[]
            bisect.insort(number[q[1]],q[2])
        tokkan.add((q[1], q[2]))

    elif q[0] == 2:
        ans = B[q[1]]
        # ans.sort()
        print(*ans)

    elif q[0] == 3:
        ans = (number[q[1]])
        # ans.sort()
        print(*ans)

