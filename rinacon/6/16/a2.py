s = input()
t = input()

ans = []

for i,j in zip(s,t):
    if i == 'Y':
        ans.append(j.upper())
    else:
        ans.append(j)

print(*ans)