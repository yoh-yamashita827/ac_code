s = list(input())
c = len(set(s))
ans = 0

if  c == 3:
    ans = 6
elif    c == 2:
    ans = 3
else:
    ans = 1

print(ans)
