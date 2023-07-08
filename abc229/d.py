from collections import deque
S = list(str(input()))
K = int(input())
n = len(S)
r,ans = 0,0
dot_count = 0

# for l in range(n):
#     while r < n :
#         if S[r] == '.':
#             dot_count += 1
#             if dot_count > K+1:
#                 r -= 1
#                 break
                
#         r += 1

#     ans = max(ans,r-l)
#     if l == r:
#         r  += 1

q = deque()
for i in S:
    q.append(i)
    if i == '.':
        dot_count += 1

    while dot_count > K:
        rm = q.popleft()
        if rm == '.':
            dot_count -= 1

    ans = max(ans, len(q))

print(ans)
