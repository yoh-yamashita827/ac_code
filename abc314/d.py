n = int(input())
# n,m = map(int,input().split())
s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#    s.append(input())
q = int(input())
from collections import defaultdict
import copy
memo = []
ans = list(copy.deepcopy(s))
last = 0
for _ in range(q):
   a,b,c = map(str,input().split())
   if int(a) == 1:
      # ans[int(b)-1] = c
      memo.append((b,c))
   else:
      last = int(a)
      for m in memo:
         ans[int(m[0])-1]=m[1]
      memo = []

if last == 3:
   ans = ''.join(ans).upper()

elif last == 2:
   ans = ''.join(ans).lower()
ans = list(ans)
if len(memo)!=0:
   for mm in memo:
      ans[int(mm[0])-1]=mm[1]  

print(''.join(ans))


