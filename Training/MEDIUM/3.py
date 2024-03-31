s=input()
nums = [0]*(len(s))
pre = s[0]
for i in range(1,len(s)-1):
    if pre == s[i]:
        nums[i] = nums[i-1]+1

print(sum(nums))