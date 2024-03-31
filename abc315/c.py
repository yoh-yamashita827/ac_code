n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
from collections import defaultdict
dic =  defaultdict(list)
f = []
s = []
for _ in range(n):
   a,b = map(int,input().split())
   f.append(a)
   s.append(b)
   dic[a].append(b)

pre = []
ans = []

for i,j in zip(f,s):
    if len(ans) != 2:
        pre.append(i)
        ans.append(j)
        continue
   
    if len(set(pre)) == 1:
        now = max(ans) + min(ans)//2
    else:
        now = sum(ans)

    pre.sort()
    ans.sort()

    tmp_f = [i,pre[1]]
    tmp_s = [j,ans[1]]

    if len(set(tmp_f)) == 1:
        tmp = max(tmp_s) + min(tmp_s)//2
    else:
        tmp = sum(tmp_s)

    if now <= tmp:
        pre = tmp_f
        ans = tmp_s


if len(set(pre)) == 1:
    now = max(ans) + min(ans)//2
else:
    now = sum(ans)

print(now)