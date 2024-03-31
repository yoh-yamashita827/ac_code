x = int(input())
ans = set()
for i in range(int(x**(1/2))+1):
    for j in range(int(x**(1/2))+1):
        if i**j <= x:
            ans.add(i**j)
print(max(ans))