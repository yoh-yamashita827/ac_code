# n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
s = input()
# # for _ in range(n):
# #     s.append(input())

# from collections import deque
# que = deque()

# for i in s:
#     if i == ')':
#         for _ in range(len(que)):
#             tmp = que.pop()
#             if tmp == '(':
#                 break

# if len(que) == 0:
#     print('Yes')
# else:
#     print('No')

s=input()
ng=[0]*26
stc=[]
for i in s:
  if i=='(':
    stc.append('(')
  elif i==')':
    while True:
      x=stc.pop()
      if x=='(':
        break
      ng[ord(x)-97]=0
  else:
    x=ord(i)-97
    if ng[x]:
      print('No')
      exit()
    ng[x]=1
    stc.append(i)

print('Yes')