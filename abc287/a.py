n = int(input())
s = []
for _ in range(n):
    s.append(input())

yes = s.count('For')
no = s.count('Against')
if yes > no:
    print('Yes')
else:
    print('No')