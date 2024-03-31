times = [int(input()) for _ in range(5)]

# ten_times = [i%10 for i in times]
import itertools
answer = 1000
for i in itertools.permutations(times):
    ans = 0
    for ii,j in enumerate(i):
        if j%10==0:
            ans += j
        else:
            if ii==4:
                ans += j
            else:
                ans += (j+(10-j%10))
    answer = min(answer,ans)
print(answer)