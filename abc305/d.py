n = int(input())
A = list(map(int,input().split()))
q = int(input())


sleep = {}
pre = 0
AA = iter([0]+A.copy())
last_time = set()
for i,v in enumerate(A):
    if i == 0:
        sleep[v] = v
        last_time.add(v)
    elif i % 2 == 1:
        sleep[v] = sleep[pre]
        pre = v
    else:
        sleep[v] = v-pre+sleep[pre]
        pre = v
        last_time.add(v)




def binary_search(N, A, x):
    l=0
    r=N-1  # A[l], A[l+1], ..., A[r] が探索範囲
    while r-l>1:  # 探索範囲の長さ r - l + 1 が 1 以上のあいだループする
        m=(l+r)//2  # (l + r) / 2 を小数点以下切り捨て
        if (A[m]) == x:
            return A[l],A[r]   
            # return A[m],0
        if (A[m]) < x:
            l = m 
        if (A[m]) > x:
            r = m 
    return A[l],A[r]



for _ in range(q):
    ans = 0
    query = list(map(int,input().split()))
    
    l,r = binary_search(n,A,query[1])
    if l not in last_time :
        ans += (sleep[l]+(query[1]-l))
    else:
        ans += sleep[l]

    l,r = binary_search(n,A,query[0])
    if l not in last_time :
        ans -= (sleep[l]+(query[0]-l))
    else:
        ans -= sleep[l]
    
    print(ans)
     

    
