from math import sqrt
n = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

sq_n = int(sqrt(n))
ans = 0
for ab in range(1,sq_n+1):
    cd = int(sqrt(n-ab))+1
    div_cd = make_divisors(cd)
    ans += (2*len(div_cd))-1

print(ans)