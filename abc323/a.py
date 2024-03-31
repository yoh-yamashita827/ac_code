# n = int(input())
# n,m = map(int,input().split())
s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

for i in range(1,len(s),2):
    if s[i] != '0':
        print('No')
        exit()

print('Yes')