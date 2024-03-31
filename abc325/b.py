n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())
time = [0]*24

for _ in range(n):
    w,x = map(int,input().split())
    time[x-1] += w

time = time+time
ans = []
for i in range(24):
    tmp = 0
    for v in time[i:i+9]:
        tmp += v

    ans.append(tmp)

print(max(ans))