n = int(input())
s=input()
ans = 0
for i in range(n):
    x = s[:i]
    y = s[i:]

    ans = max(ans,len(set(list(x))&set(list(y))))
    
print(ans)