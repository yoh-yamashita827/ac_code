n,k = map(int,input().split())
A = []
B = []
AB = []
for _ in range(n):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

m_benefit = []
for i,j in zip(A,B):
    m_benefit.append(i-j)

m_benefit = B + m_benefit

m_benefit.sort(reverse=True)

ans = 0
for i in range(k):
    ans += m_benefit[i]

print(ans)