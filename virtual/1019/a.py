# n = int(input())
h,w = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
a = [list(map(int,input().split())) for _ in range(h) ]
# for _ in range(n):
#     s.append(input())

for i in (list(map(list, (zip(*a))))):
    print(*i)