from collections import Counter
N = int(input())
S = []
for i in range(N):
    S.append(input())

cnt = Counter(S)

print(cnt.most_common()[0][0])

