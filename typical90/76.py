n = int(input())
A = list(map(int,input().split()))

def shaku(A: list) -> bool:
    l = r = 0
    if sum(A)%10 != 0:
        return False

    base = sum(A)//10

    cake = A+A
    mp = [0]
    for i,v in enumerate(cake):
        mp.append(mp[i]+v)

    while(r<2*n):
        if mp[r]-mp[l] < base:
            r += 1
        elif mp[r]-mp[l] == base:
            if (r-l) > n:
                continue
            return True
        else:
            l += 1

    return False


if shaku(A):
    print('Yes')
else:
    print('No')