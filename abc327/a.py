n = int(input())
s = input()
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

for i in range(n-1):
    window = s[i:i+2]

    if (window == 'ab') or (window == 'ba'):
        print('Yes')
        exit()

print('No')