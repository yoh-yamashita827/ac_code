# n = int(input())
n,m,p = map(int,input().split())
# s = input()
a = list(map(int,input().split()))
b = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())
if n > m:
    a,b = b,a
    n,m = m,n

def binary(A,x):
    l = 0
    r = len(A)

    while(r!=l):
        m = (r+l)//2
        if A[m] >= x:
            r = m
        else:
            l = m+1    
    return r


# cnt = 2*sum(a) + 2*sum(b)
ans = 0
b.sort()



from collections import defaultdict
b_dic = defaultdict(int)
r = 0
for j,v in enumerate(b):
    r += v
    b_dic[j] = r
b_sum = sum(b)
for i in a:
    tmp = binary(b,p-i)
    if tmp == m:
        ans += i*tmp + b_sum
    else:ans += (i*tmp)+(b_dic[tmp-1])+p*(m-tmp)

print(ans)
    