n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

for i in range(n,920):
    tmp = list(str(i))
    tmp = [int(i) for  i in tmp]
    if tmp[0]*tmp[1] == tmp[2]:
        print(i)
        exit()
    