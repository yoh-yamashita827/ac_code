# n = int(input())
n,m = map(int,input().split())
# s = input()
l = list(map(int,input().split()))
# s = []
# for _ in range(n):
#    s.append(input())

total = sum(l)+(n-1)
max_w = total//m

ans = 0

for i in l:
    if (max_w < ans+i):
        max_w = ans+i

        # ans += l
        ans = 0
        
    else:
        ans += i+1

print(max_w)