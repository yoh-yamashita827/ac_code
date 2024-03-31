# n = int(input())
M,D = map(int,input().split())
y,m,d = map(int,input().split())
# s = input()
# A = list(map(int,input().split()))
# s = [input() for _  in range(n)]

if M==m and D==d:
    print(y+1,1,1)
elif D==d:
    print(y,m+1,1)
else:
    print(y,m,d+1)



