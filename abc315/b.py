m = int(input())
# n,m = map(int,input().split())
# s = input()
d= list(map(int,input().split()))
# s = []
# for _ in range(n):
#    s.append(input())

total = sum(d)
mid = (total+1)//2
cnt = 0
month = 0
day = 0
for i,v in enumerate(d):
    if cnt + v < mid:
        cnt += v

    else:
        month = i+1
        day = mid-cnt
        break

print(month,day)


    