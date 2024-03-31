# n = int(input())
# n,m = map(int,input().split())
s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#    s.append(input())
ans = 1
for i in range(len(s)):
    for j in range(i,len(s)+1):
        window = s[i:j]

        if window == window[::-1]:
            ans = max(ans,len(window))

print(ans)