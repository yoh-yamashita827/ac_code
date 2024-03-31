# n = int(input())
# n,m = map(int,input().split())
s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

from collections import deque
S = [ord(i) for i in s]
S = deque(s)
flg = True
ans = ''
while(flg):
    flg = False
    for i in s:
        ans += i
        if ans[::-1][0:3] == 'CBA':
            ans = ans[:-3]
            flg = True
print(ans)
# for i in s:
#     if i=='A':
#         tmp = ['A']

#     else:
#         if tmp != []:
#             tmp.append(i)
#             if len(tmp) >= 4:
#                 ans += tmp.pop()
#             if tmp == ['A','B','C']:
#                 tmp = []
#                 for j in reversed(ans):
#                     if j == 'A':
#                         break

#         else:
#             ans += i
#             tmp = []
# print(S)
