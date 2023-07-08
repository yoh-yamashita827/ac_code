from collections import Counter
n = int(input())
A = list(map(int,input().split()))

matching = Counter(A)
cnt = 0
for key in matching.keys():
    num = matching[key]
    cnt += (num // 2)

print(cnt)

