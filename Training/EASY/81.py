def cnt_div2(x):
    cnt = 0
    while(True):
        if x%2 == 0:
            x /= 2
            cnt += 1
        else:
            break
    return cnt

n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in a:
    ans += cnt_div2(i)
print(ans)