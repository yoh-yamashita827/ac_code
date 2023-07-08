N,M = map(int,input().split())
a = []
b = []
num = 0
ans = 1
def fb(num):
    """num番目のフィボナッチ数を返す
    """#[1,1,2,3..]
    a, b = 1, 0
    for _ in range(num):
        a, b = a + b, a
    return b

if M == 0:
    print(fb(N%1000000007)%1000000007)
    exit(0)
else:
    for i in range(M):
     a.append(int(input()))

for i in range(len(a)-1):
    if  a[i+1] - a[i] == 1:
        print(0)
        exit(0)



b.append(a[0])

for i in range(M-1):
    b.append(a[i+1]-a[i])



for i in range(1,len(b)):
    ans *= (fb(b[i]-1) % 1000000007)
ans *= (fb(b[0])%1000000007)
ans *= (fb(N-a[-1])%1000000007)


print(ans%1000000007)

