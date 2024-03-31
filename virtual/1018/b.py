import itertools
n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
s = [input() for _ in range(n)]
# for _ in range(n):
#     s.append(input())

for i in itertools.combinations(s,2):
    tmp = i[0]+i[1]
    tmp2 = i[1]+i[0]

    if tmp == tmp[::-1]:
        print('Yes')
        exit()

    if tmp2 == tmp2[::-1]:
        print('Yes')
        exit()

print('No')