import sys
sys.setrecursionlimit(10**9)
n = int(input())
from typing import Dict

fib_memo: Dict[int, int] = {0: 2, 1: 1}

def lucas(n: int) -> int:
    if n not in fib_memo.keys():
        fib_memo[n] = lucas(n-2) + lucas(n-1)
    return fib_memo[n]
    
print(lucas(n))