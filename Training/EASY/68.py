n = int(input())
rest = {}
nums = {}
cnt = 1
for _ in range(n):
    s,p = map(str,input().split())
    nums[int(p)] = cnt
    if s not in rest.keys():
        rest[s] = [int(p)]
    else:
        rest[s].append(int(p))

    cnt += 1

rest = dict(sorted(rest.items()))
# rest = dict(sorted(rest.values(), key=lambda x:x[1]))

for i in rest.values():
    i.sort(reverse=True)
    for j in i:
        print(nums[j])