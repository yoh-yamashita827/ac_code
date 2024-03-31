H, M = map(str,input().split())

def make(h,m):
    ab = list(str(h).zfill(2))
    cd = list(str(m).zfill(2))

    return ab[0],ab[1],cd[0],cd[1]

def judge(a,b,c,d):
    ac = int(a+c)
    bd = int(b+d)

    return (0 <= ac <= 23) and (0 <= bd <= 59)

def clock(a,b,c,d):
    h = int(a+b)
    m = int(c+d)

    if m+1 < 60:
        return make(h,m+1)
    
    if h+1 < 24:
        return make(h+1,0)
    else:
        return make(0,0)


a,b,c,d = make(H,M)
if judge(a,b,c,d):
    print(a+b,c+d)
    exit()

while(judge(a,b,c,d) == False):
    a,b,c,d = clock(a,b,c,d)

print(a+b,c+d)


