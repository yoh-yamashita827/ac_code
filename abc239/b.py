import math
from decimal import *

n = int(input())

if n % 10 == 0:
    print(int(Decimal(n)/Decimal(10)))
    exit(0)

elif n > 0:
    print(math.floor(Decimal(n)/Decimal(10)))
    exit(0)

else:
    print(math.floor(Decimal(n)/Decimal(10)))
    exit(0)