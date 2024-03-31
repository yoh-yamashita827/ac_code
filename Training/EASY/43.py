s = input()

gu = [s.count(i)%2 for i in s]

if sum(gu) == 0:
    print('Yes')
else:
    print('No')