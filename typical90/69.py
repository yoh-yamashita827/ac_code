n,k = map(int,input().split())

mod = 10**9 + 7

if n == 1:
    print(k)
    exit()
elif n == 2:
    print(k*(k-1))
    exit()

ans = k*(k-1)*pow(k-2,n-2,mod)

print(ans%mod)