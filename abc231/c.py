N,Q = map(int,input().split())
A = list(map(int,input().split()))
x = []
for i in range(Q):
    x.append(int(input()))

A.sort()


def binary_search(data, value):
    left = 0            # 探索する範囲の左端を設定
    right = len(data) - 1            # 探索する範囲の右端を設定
    while right >= left :
        mid = (left + right) // 2            # 探索する範囲の中央を計算
        if data[mid] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid - 1
    return left 


for i in x:
    print(N-(binary_search(A,i)))