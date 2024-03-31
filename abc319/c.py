# n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
import itertools
c = [list(map(int,input().split())) for _ in range(3)]
grid = []
for i in c:
    grid.extend(i)

from collections import defaultdict
nums = defaultdict(int)
for i in grid:
    nums[i] += 1

for i in nums.values():
    if i == 1:
        continue
    else:
        ans += 1

def judge(x):
    pre = 0
    for v,k  in enumerate(x):
        if pre == k:
            if v != len(x):
                return 1
        pre = k

    return 0

# for _ in range(n):
#    s.append(input())
total = len(list(itertools.permutations(grid,9)))
ans = 0
for i in itertools.permutations(grid):
    if judge(i):
        ans += 1

print((total-ans)/total)