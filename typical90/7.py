n  = int(input())
A = list(map(int,input().split()))
q = int(input())
A_sort = sorted(A)


def binary_search(N, A, x):
    l=0
    r=N-1  # A[l], A[l+1], ..., A[r] が探索範囲
    while r-l>1:  # 探索範囲の長さ r - l + 1 が 1 以上のあいだループする
        m=(l+r)//2  # (l + r) / 2 を小数点以下切り捨て
        if (A[m]) == x:
            return 0
        if (A[m]) < x:
            l = m 
        if (A[m]) > x:
            r = m 
    return min(abs(A[l]-x),abs(A[r]-x))

for i in range(q):
    b = int(input())
    near = binary_search(n,A_sort,b)

    print(near)

