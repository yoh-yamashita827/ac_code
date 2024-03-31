n,k = map(int,input().split())
s = input()
ans = ''
cnt = 0
for i in s:
    if cnt < k:
        if i == 'o':
            cnt += 1
        ans += i
    else:
        ans += 'x'

print(ans)
