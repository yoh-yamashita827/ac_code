n,x = map(int,input().split())
a = list(map(int,input().split()))

aa = sorted(a)

def binary_search(N, A, x,i):
    l=0
    r=N-1  # A[l], A[l+1], ..., A[r] が探索範囲
    while r-l+1>=1:  # 探索範囲の長さ r - l + 1 が 1 以上のあいだループする
        m=(l+r)//2  # (l + r) / 2 を小数点以下切り捨て
        if (i-A[m]) == x:
            return 1
        if (i-A[m]) < x:
            r = m - 1
            # l = m + 1
        if (i-A[m]) > x:
            l = m + 1
            # r = m - 1
    return 0

for i in aa:
    if binary_search(n,aa,x,i):
        print('Yes')
        exit()
print('No')
    

