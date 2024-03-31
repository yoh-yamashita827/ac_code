n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

for i in range(1,16):
    if pow(i,i) == n:
        print(i)
        exit()

print(-1)