# n = int(input())
# n,m = map(int,input().split())
s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

cnt = len(s)
pre = '-1'
tmp = 0
for i in s:
    if (i == '0') and (pre == '0'):
        tmp += 1
        continue

    pre = str(i)
    if tmp == 0:continue
    cnt -= (tmp+1)//2
    tmp =  0

if tmp != 0:
    print(cnt - (tmp+1)//2)
else:
    print(cnt)
# r,l, ans = 0, 0, 0
# while(r < len(s)-1):
#     while s[r] == '0':
#         r += 1

#     if l == r:
#         r += 1
#     else:
#         cnt -= (r-(l+1))//2
#         l = r
        

