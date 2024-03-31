n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
s = [input() for _ in range(n)]
# for _ in range(n):
#     s.append(input())

from collections import defaultdict

names = {}

for i in s:
    if i not in names.keys():
        names[i] = 0
        print(i)

    else:
        names[i] += 1
        print(i+'({})'.format(names[i]))
