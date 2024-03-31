# n = int(input())
# n,m = map(int,input().split())
s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#    s.append(input())
ans = ''
a = ['a','i','u','e','o']
for i in s:
    if i in a:
        continue
    ans += i

print(''.join(ans))