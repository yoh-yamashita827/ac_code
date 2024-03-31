n = (input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())
pre = 10
for i in n:
    if pre <= int(i):
        print('No')
        exit()

    pre = int(i)

print('Yes')