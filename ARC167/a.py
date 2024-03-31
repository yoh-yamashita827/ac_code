n,m = map(int,input().split())
A = list(map(int,input().split()))

A.sort(reverse=True)

def anbalance(X):
    ans = 0
    for i in X:
        ans += (i**2)

    return ans

dishes = [0]*m

for i in range(m):
    dishes[i] += A.pop(0)

id = m-1
while(len(A)!=0):
    tmp = A.pop(0)
    dishes[id] += tmp
    id -= 1


print(anbalance(dishes))

