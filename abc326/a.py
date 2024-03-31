# n = int(input())
x,y = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

tmp = (y-x)
ans = 'Yes'
if tmp > 0:
    if abs(tmp) <= 2:
        print(ans)
        exit()
elif abs(tmp) <= 3:
    print(ans)
    exit()
print('No')
