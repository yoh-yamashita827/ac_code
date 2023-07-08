from decimal import Decimal

N = int(input())
AB = []
A = []
B = []
for _ in range(N):
    a,b = map(int,input().split())
    AB.append([a,b])
    A.append(a)
    B.append(b)

def acc(a,b):
    return Decimal(str(a))/Decimal(str((a+b)))

ans = {}

for i in range(N):
    a,b = AB[i]
    rate = acc(a,b)
    ans[i] = rate

sort_ans = sorted(ans.items(), key = lambda ans : ans[1],reverse=True)

num = []
pre = 0
for i in sort_ans:
    num.append(i[0]+1)

print(*num)


