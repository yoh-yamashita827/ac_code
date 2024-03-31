# n = int(input())
n,x = map(int,input().split())
# s = input()
c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

ans = 0
for i in c:
    if i <= x:
        ans += i
print(ans)
