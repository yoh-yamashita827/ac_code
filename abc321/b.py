# n = int(input())
n,x = map(int,input().split())
# s = input()
a = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())



def judge(A):
    A.sort()
    if sum(A[1:n-1])-x >= 0:
        return sum(A[1:n-1])-x
    else:
        return -1
    
for i in range(101):
    a.append(i)
    tmp = judge(a)
    if tmp != -1:
        print(i)
        exit()
    a.remove(i)

print(-1)