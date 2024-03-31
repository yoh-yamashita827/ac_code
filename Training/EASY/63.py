from collections import deque
n = int(input())
a = list(map(int,input().split()))
que=deque(a)
cnt = 0
i = 1
while(que):
    if que.popleft() != i:
        cnt += 1

    else:
        i += 1

if cnt != n:
    print(cnt)
else:
    print(-1)