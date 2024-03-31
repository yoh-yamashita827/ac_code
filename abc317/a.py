# n = int(input())
n,h,x = map(int,input().split())
# s = input()
p = list(map(int,input().split()))
# s = []
# for _ in range(n):
#    s.append(input())

for i,v in enumerate(p):
    if h+v >= x:
        print(i+1)
        exit()
