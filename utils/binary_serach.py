def binary_search(N, A, x):
    l=0
    r=N-1  # A[l], A[l+1], ..., A[r] が探索範囲
    while r-l+1>=1:  # 探索範囲の長さ r - l + 1 が 1 以上のあいだループする
        m=(l+r)//2  # (l + r) / 2 を小数点以下切り捨て
        if (A[m]) == x:
            return 1
        if (A[m]) < x:
            r = m - 1
            # l = m + 1
        if (A[m]) > x:
            l = m + 1
            # r = m - 1
    return 0