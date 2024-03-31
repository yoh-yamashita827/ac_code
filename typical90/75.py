def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

import math
n = int(input())
fact = (prime_factorize(n))


if len(fact) == 1:
    print(0)

else:
    print(math.ceil(math.log2(len(fact))))