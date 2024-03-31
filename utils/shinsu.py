def X_To_Ten(N: int,x: int) -> int:
    if N < 10:
        return N
    else:
        div, mod = divmod(N, 10)
        return mod + x * X_To_Ten(div)


def ten_To_X(N: int,x: int) -> int:
    res = 0
    level = 0
    while N:
        div, mod = divmod(N, x)
        res += mod * (10**level)
        N = div
        level += 1
    return res