from collections import deque
n,q = map(int,input().split())

# cus = set(list(range(1,n+1)))
waiting = set()
cnt = 1
for i in range(q):
    call = list(map(int,input().split()))
    if call[0] == 1:
        # waiting.add(cus.popleft())
        waiting.add(cnt)
        cnt += 1
    elif call[0] == 2:
        waiting.remove(call[1])
    elif call[0] == 3:
        print(min(waiting))

