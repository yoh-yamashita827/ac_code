N, M = map(int, input().split())
P = [list(map(int, input().split())) for i in range(N)]
total = []
rank = 0
cnt = 0

for j in range(N):
    total.append(sum(P[j]))

total_sort = sorted(total, reverse = True)


for i in range(N):
    if total_sort[M-1] - total[i] <= 300:
        print('Yes')
    else:
        print('No')

