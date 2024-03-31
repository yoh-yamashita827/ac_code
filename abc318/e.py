n = int(input())
A = list(map(int,input().split()))

nums = {}
for i,v in enumerate(A):
    if v not in nums.keys():
        nums[v] = [i]

    elif len(nums[v]) == 1:
        nums[v].append(i)

    else:nums[v][-1] = i

ans = 0
for val in nums.values():
    if len(val) == 1:
        continue
    ans += (val[1]-val[0]-1)

print(ans)