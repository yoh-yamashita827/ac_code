n = int(input())
u = list(map(int,input().split()))
import heapq
from heapq import heapify,heappop,heappush
heapq.heapify(u)

while(len(u)!=1):
    a = heappop(u)
    b = heappop(u)

    new = (a+b)/2
    heappush(u,new)

print(heappop(u))