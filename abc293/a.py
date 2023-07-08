s = input()
it = iter(s)
ans = []
for i, j in zip(it, it):
    ans.append(j)
    ans.append(i)

print(''.join(ans))
