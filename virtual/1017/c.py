# n = int(input())
n,m = map(int,input().split())
# s = input()
a = list(map(int,input().split()))
b = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())


def binary(x,A):
    l = 0
    r = len(A)

    while(r!=l):
        m = (r+l)//2

        if A[m] >= x:
            r = m

        else:
            l = m+1

    return r+1

c = a+b
c.sort()

ans= []
for i in a:
    ans.append(binary(i,c))
print(*ans)

ans = []
for i in b:
    ans.append(binary(i,c))
print(*ans)