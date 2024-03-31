n = int(input())
# n,m = map(int,input().split())
s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

window = ['A','B','C']

for i in range(n-2):
    tmp = list(s[i:i+3])
    if tmp == window:
        print(i+1)
        exit()

print(-1)