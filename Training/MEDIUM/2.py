s=input()
# from collections import deque
# que=deque()

# cnt = 0
# tmp = 0
# for i in s:
#     if i == 'W':
#         que.append(i)
#     else:
#         if len(que):
#             break

mt = [0]*len(s)
if s[0] == 'B':
    mt[0] = 1
for i in range(1,len(s)):
    if s[i] == 'B':
        mt[i] = mt[i-1] + 1

    else:
        mt[i] = mt[i-1]

ans = 0
for i in range(len(s)):
    if s[i] == 'W':
        ans += mt[i]

print(ans)