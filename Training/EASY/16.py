n = int(input())
a=list(map(int,input().split()))

nums = {i+1:a[i] for i in range(n)}


nums2 = sorted(nums.items(),key=lambda x:x[1])

print(*(list(dict(nums2).keys())))