# n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#    s.append(input())


from functools import lru_cache


@lru_cache
def f(n):
    if n == 0:
        return 1
    return f(n // 2) + f(n // 3)


print(f(int(input())))
