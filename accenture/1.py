#　拡張
from collections import Counter
from collections import deque

n,k = map(int,input().split())
a = list(map(int,input().split()))


que=deque()
que = deque(a)
target = deque()
for i in range(k):
    target.append(que.popleft())
counter = Counter(target)
max_count = max(counter.values())
modes = ([num for num, count in counter.items() if count == max_count])
print(min(modes))
for i in range(k,n):
    Out = target.popleft()
    counter[Out] -= 1
    In = que.popleft()
    counter[In] += 1

    max_count = max(counter.values())
    modes = ([num for num, count in counter.items() if count == max_count]) 
    print(min(modes))

