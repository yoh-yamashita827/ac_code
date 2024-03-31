# n = int(input())
a,b = map(int,input().split())
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

num = b/a

print(Decimal(str(num)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))


