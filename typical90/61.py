q = int(input())
from collections import deque
deck = deque()
for _ in range(q):
    t,x = map(int,input().split())
    if t == 1:
        deck.appendleft(x)
    elif t == 2:
        deck.append(x)
    else:
        print(deck[x-1])