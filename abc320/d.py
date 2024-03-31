m = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
from collections import defaultdict
s = []
for _ in range(3):
    s.append(input())

if s[0] == s[1] == s[2]:
    print(m)
    exit()

reel1 = defaultdict(list)
reel2 = defaultdict(list)
reel3 = defaultdict(list)

for i,v in enumerate(s[0]):
    reel1[v].append(i)
for i,v in enumerate(s[1]):
    reel2[v].append(i)
for i,v in enumerate(s[2]):
    reel3[v].append(i)

num1 = set()
for i in s[0]:
    num1.add(i)
num2 = set()
for i in s[1]:
    num2.add(i)
num3 = set()
for i in s[2]:
    num3.add(i)

check = defaultdict(int)
for i in num1:
    check[i] += 1
for i in num2:
    check[i] += 1
for i in num3:
    check[i] += 1

flg = False
for i in check.keys():
    if check[i] >= 3:
        flg = True

if not flg:
    print(-1)
    exit()


ans = 200
for i in reel1.keys():
    for j in reel2.keys():
        for k in reel3.keys():
            if not (i==j==k):continue

            ans = min(ans,max(reel1[i]+reel2[j]+reel3[k]))
         

print(ans)