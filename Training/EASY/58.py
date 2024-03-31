n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))

temp = [t-(i*0.006) for i in h]
sub_temp = [abs(a-i) for i in temp]

ans = INF=float('inf')
cnt = 0
for i,v in enumerate(sub_temp):
    if ans > v:
        cnt = i

        ans = v

print(cnt+1)