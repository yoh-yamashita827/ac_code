a,b,k = map(int,input().split())
numbs = []
if (b-a) <= k:
    for i in range(a,b+1):
        print(i)

    exit()
for i in range(a,a+k):
    numbs.append(i)

for i in range(b-(k-1),b+1):
    numbs.append(i)

nums = list(set(numbs))
nums.sort()

for i in nums:
    print(i)