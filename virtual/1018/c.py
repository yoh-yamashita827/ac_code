# n = int(input())
# n,m = map(int,input().split())
s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())
charge = []
cnt = 0
for i in reversed(s):
    if (i != '0'):
        cnt += 1
        cnt += (len(charge)+1)//2
        charge = []
        continue

    charge.append(i)

print(cnt)