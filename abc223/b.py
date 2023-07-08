from collections import deque

S = list(input())
S = deque()

for i in range(len(S)):
    a = S.pop()
    S.append(str(a))

    for i in range(S):
        


