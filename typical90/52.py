n = int(input())
A = []
for i in range(n):
    A.append(sum(list(map(int,input().split()))))
mod = 10**9 + 7
ans = 1
for i in A:
    ans *= i

print(ans%mod)


