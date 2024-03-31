n = int(input())
s=input()

s = [1 if i=='I' else -1 for i in s]
x = 0
ans = []
for i in s:
    x += i
    ans.append(x)

print(max(0,max(ans)))