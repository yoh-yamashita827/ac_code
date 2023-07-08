from decimal import Decimal, ROUND_HALF_UP
def my_round(num, k):
    keta = '1E'+str(k)
    return Decimal(str(num)).quantize(Decimal(keta), rounding=ROUND_HALF_UP)

X, K = map(int,input().split())
ans = X

for i in range(0,K):
    ans = int(my_round(ans,i+1))

print(ans)