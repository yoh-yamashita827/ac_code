# l,r = map(int,input().split())

# mod = 10**7 + 1

# ans = 0

# def sn(x):
#     return (x*(x+1))//2


# while(r!= l):
#     if len(str(l)) != len(str(r)):
#         ans += len(str(l)) * (sn(10**len(str(l))-1)-sn(l-1))
#         ans %= mod

#         l = 10**(len(str(l)))
#         if l == r:
#             ans += len(str(l))*l
#             ans %= mod
#     else:
#         ans += len(str(l)) * (sn(r)-sn(l-1))
#         ans %= mod
#         l = r

# print(ans%mod)

import sys

def main(f):
  L,R = map(int, f.readline().split())
  mod = 10 ** 9 + 7
  min_digit = len(str(L))  # xの範囲で最も小さい桁数
  max_digit = len(str(R))  # xの範囲で最も大きい桁数
  ans = 0
  for i in range(min_digit, max_digit+1):
    min_num = max(L, 10 ** (i - 1))  # 同じ桁の中での最小値（等差数列の初項）。基本は10 ** (i - 1)だがLが含まれる桁ではLが最小値
    max_num = min(R, 10 ** i - 1)  # 同じ桁の中での最大値（等差数列の末項）。基本は10 ** i - 1だがRが含まれる桁ではRが最大値
    num = max_num - min_num + 1  # 数列の項数
        
    ans += num * (min_num + max_num) // 2  * i
    
  print(int(ans % mod))
    
main(sys.stdin)